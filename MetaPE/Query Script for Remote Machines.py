'''
Query info on a huge number of remote machines
目标：
编写脚本从大量远程机器上收集某些信息。
信息可以是系统状态、硬件配置、日志文件等。
考虑远程机器数量庞大时的性能和资源管理问题。
关键点：
如何高效、并发地从大量机器获取信息。
如何处理可能的网络延迟、连接失败或部分机器不可达的问题。
脚本是否支持扩展，比如可配置查询的命令或输出格式。
'''
import paramiko
import concurrent.futures

# Connect to remote machine via SSH, execute a command and return the result
# Return a message if the connection fails or success
def query_remote_machine(host, user, password, command):
  try:
    # Create a SSH client
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) # Auto add unknown host keys
    ssh.connect(host, username=user, password=password, timeout=5) # Connect to remote machine
    
    # Execute the command
    stdin, stdout, stderr = ssh.exec_command(command)
    result = stdout.read().decode().strip() # Read and decode the result
    error = stderr.read().decode().strip() # Read and decode the error
    
    ssh.close() # Close the SSH connection
    
    if error:
      return f"Error on {host}: {error}"
    return f"Success on {host}: {result}"
  
  except Exception as e:
    # Catch any exception that occurs and return an error msg
    return f"Connection failed on {host}: {str(e)}"

# Query a list of remote machines in parallel using a thread pool
# max_workers: Maximum number of threads to use
def query_machines_in_paraller(machine_list, user, password, command, max_workers=10):
  results = []
  with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
    # Submit tasks for each machine to the thread pool
    future_to_host = {executor.submit(query_remote_machine, host, user, password, command): host for host in machine_list}
    
    # Process the results as they completed
    for future in concurrent.futures.as_completed(future_to_host):
      host = future_to_host[future] # Get the host corresponding to this future
      try:
        result = future.result() # Get the result of the query
        results.append(result) 
      except Exception as e:
        results.append(f"Error on {host}: {str(e)}")
  return results

if __name__ == "__main__":
  # Define the input parameters
  machine_list = ["192.168.1.101", "192.168.1.102", "192.168.1.103"]
  user = "username"
  password = "password"
  command = "uptime"
  
  # Execute the queries in parallel
  results = query_machines_in_paraller(machine_list, user, password, command)
  
  # Save the results to a file
  output_file = "query_results.txt"
  with open(output_file, 'w') as file:
    for result in results:
      file.write(result + "\n") # Write each result to a new line
  # Print a message indicate the query is complete
  print(f"Query completed. Results saved to {output_file}.")
    