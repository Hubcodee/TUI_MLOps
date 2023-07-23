import subprocess

# Replace 'hadoop' with the actual path to your 'hadoop' binary if it's not in the system PATH
hadoop_bin = 'hadoop'

# HDFS file path to read (replace with your actual HDFS file path)
hdfs_file_path = "/demo/lr.csv"

try:
    cat = subprocess.Popen([hadoop_bin, "fs", "-cat", hdfs_file_path], stdout=subprocess.PIPE, text=True)
    stdout, stderr = cat.communicate()

    if cat.returncode == 0:
        # 'stdout' variable now contains the content of the HDFS file
        print(stdout)
    else:
        print(f"Error executing the Hadoop command. Error message: {stderr}")
except Exception as e:
    print(f"An error occurred: {e}")
