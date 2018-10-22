'''
Developer : Shashank Sharma
Contributors : 

Main File : Run this file to Create Batch Certificates
'''
import sys
import os

sys.path.insert(0,os.getcwd()+'\Scripts')
import BatchCertificateMaker as cert


cert.createBatchCertificates()