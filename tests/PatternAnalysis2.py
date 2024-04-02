import numpy as np
import os
from collections import Counter
from context_encryption7 import encrypt_data_aes_gcm, derive_secure_key, get_enhanced_contextual_data

def calculate_entropy(data):
    """Calculate the Shannon entropy of the given data."""
    if not data:
        return 0
    data_counts = Counter(data)
    probabilities = [count / len(data) for count in data_counts.values()]
    entropy = -sum(p * np.log2(p) if p > 0 else 0 for p in probabilities)
    return entropy

def generate_structured_data_patterns(samples=100):
    """Generates structured data samples reflecting real-world patterns."""
    patterns = [
        "admin_password", 
        "<xml><data>Example</data></xml>", 
        '{"key": "value", "status": "active"}', 
        "123-456-789", 
        "user@example.com"
    ]
    
    # Generate combinations of patterns with varying repetitions to simulate structured data
    structured_data_samples = [pattern * np.random.randint(1, 5) for pattern in patterns for _ in range(samples // len(patterns))]
    return structured_data_samples

def test_entropy_across_patterns():
    """Test entropy for different structured data patterns."""
    secure_key = derive_secure_key(get_enhanced_contextual_data())
    structured_data_samples = generate_structured_data_patterns()
    entropy_results = []

    for data in structured_data_samples:
        # Note: encrypt_data function should be adjusted if it takes different parameters or data type
        encrypted_data = encrypt_data_aes_gcm(data, secure_key)
        entropy = calculate_entropy(encrypted_data)
        entropy_results.append(entropy)

    avg_entropy = np.mean(entropy_results)
    print(f"Average Entropy across patterns: {avg_entropy:.4f}")
    return entropy_results

if __name__ == "__main__":
    entropy_results = test_entropy_across_patterns()
    for entropy in entropy_results[:10]:  # Display the first 10 results for brevity
        print(f"Entropy: {entropy:.4f}")