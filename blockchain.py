# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 14:29:24 2020

@author: Rachit
"""
import datetime
import hashlib
import json
from flask import Flask, jsonify

#creation of genesis and inititalisation of blockchain

class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_block(proof = 1, prev_hash = '0') #genesis block 
        
        #create a block function used to append the mined block in the blockchain
    def create_block(self, proof, prev_hash):
        block ={
            'index' : len(self.chain) + 1,
            'timestamp' : datetime.datetime.now,
            'proof': proof,
            'prev_hash':prev_hash}
        self.chain.append(block)
        return block
    
    #create a function to get access to the previous block
    
    def get_prev_block(self):
        return self.chain[-1]
                            
    def proof_of_work(self, prev_proof):
        new_proof = 1
        check_proof = False
        while check_proof is False:
            hash_operation = hashlib.sha256(str(new_proof**2-prev_proof**2).encode()).hexdigest()
            if hash_operation[:4] == '0000':
                check_proof = True
            else:
                new_proof = new_proof + 1
            return new_proof
        
    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys = True).encode()
        return hashlib.sha256(encoded_block).hexdigest()
    
    x
        