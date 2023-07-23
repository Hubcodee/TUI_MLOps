from art import text2art
import os
from colorama import Fore
import csv
import requests

API_HOST ="http://192.168.56.101:5000/model"

def read_res():
    filepath = '/tmp/result.txt'
    with open(filepath,'r') as f:
        data = f.read()
        print(data)

def mains():
    Art=text2art("Team Innov-AI-te")
    print(Fore.LIGHTBLUE_EX + Art)
    print(Fore.LIGHTYELLOW_EX + "1. Linear Regression Path: (DATASET: lr)")
    print(Fore.LIGHTYELLOW_EX + "2. Logistic Regression: (DATASET: LogR) ")
    print(Fore.LIGHTYELLOW_EX + "3. Multi-Linear Regression Path: ")
    print(Fore.LIGHTYELLOW_EX + "4. Artifical Neural Network Path: ")
    x = int(input('Enter the option: '))
    if x==1:
        path = input("Enter the Linear Regression Path: ")
        type_name = 'LR' 
        print("Your request is made....")
        print("wait for results: ")
        response = requests.get(f"{API_HOST}?type_name={type_name}&dataset_name={path}")
        # print(response)
        os.system("docker cp LR:/app/result.txt /tmp/result.txt")
        read_res()
    elif x==2:
        path = input("Enter the Logistic Regression Path: ")
        type_name = 'LogR' 
        print("Your request is made....")
        print("wait for results: ")
        response = requests.get(f"{API_HOST}?type_name={type_name}&dataset_name={path}")
        # print(response)
        os.system("docker cp LogR:/app/result.txt /tmp/result.txt")
        read_res()
    elif x==3:
        path = input("Enter the Multi-Linear Regression Path: ")
        print("Under Development ....")
    elif x==4:
        path = input("Enter the Nueral Network Dataset Path: (Dataset: NN.csv) ")
        type_name = 'NN' 
        print("Your request is made....")
        print("wait for results: ")
        response = requests.get(f"{API_HOST}?type_name={type_name}&dataset_name={path}")
        # print(response)
        os.system("docker cp NN:/app/result.txt /tmp/result.txt")
        read_res()      
    y = input("Do you want to see the options again (y/n): ").lower()
    if y=='y':
        os.system('clear')
        mains()
    else:
        os.system('clear')
        exit()


if __name__=="__main__":
    mains()