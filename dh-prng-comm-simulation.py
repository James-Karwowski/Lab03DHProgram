import hashlib
import os

class SecurePRNG:
  # Required methods for the PRNG go here
  def __init__(self, seed):
    # Initialize 32-byte state using SHA-256 of the DH secret
    self.state = hashlib.sha256(str(seed).encode()).digest()

  def generate(self, n_value):
    keystream = b""
    while len(keystream < n_value):
      # Hash current state to produce output
      output = hashlib.sha256(self.state).digest()
      keystream += output
      # Rollback Resistance: Update state with a new hash
      self.state = hashlib.sha256(output + self.state).digest()
    return keystream[n_value]

  def stream_cipher(message_in_bytes, prng):
    keystream = prng.generate(len(message_bytes))
    return bytes([b ^ k for b, k in zip(message_bytes, keystream)])

class Entity:
  # Required methods for Entity go here

class Attacker:
  # Required methods for Mallory (the attacker) go here

class Network:
  # Required methods to simulate the Network go here

def run_prng_sim(is_mitm_scenario=False):
  # Main method for running the simulations
  
if __name__ == "__main__":
  run_prng_sim(is_mitm_scenario=False)
  run_prng_sim(is_mitm_scenario=True)
