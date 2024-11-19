import subprocess


def bytes_to_mbps(bytes_per_sec):
    return (bytes_per_sec * 8) / 1_000_000  # Convert to Mbps

def measure_speed(test_url, upload_file=None):
    try:
        # Download Speed Test
        if upload_file is None:
            download_command = [
                "curl", "-s", "-w", 
                "Download Speed: %{speed_download} bytes/sec\\n", 
                "-o", "/dev/null", 
                test_url
            ]
            download_result = subprocess.run(download_command, capture_output=True, text=True)
            output = download_result.stdout
            print(output)

            # Extract speed value from the output
            speed_bytes = float(output.split(":")[1].strip().split()[0])
            speed_mbps = bytes_to_mbps(speed_bytes)
            print(f"Download Speed: {speed_mbps:.2f} Mbps")
        
        # Upload Speed Test
        else:
            upload_command = [
                "curl", "-s", "-w", 
                "Upload Speed: %{speed_upload} bytes/sec\\n", 
                "-o", "/dev/null", 
                "-F", f"file=@{upload_file}", 
                test_url
            ]
            upload_result = subprocess.run(upload_command, capture_output=True, text=True)
            output = upload_result.stdout
            print(output)

            # Extract speed value from the output
            speed_bytes = float(output.split(":")[1].strip().split()[0])
            speed_mbps = bytes_to_mbps(speed_bytes)
            print(f"Upload Speed: {speed_mbps:.2f} Mbps")

    except Exception as e:
        print(f"Error: {e}")

# Example usage
test_url = "https://github.com/lyn-93/Speed_Test/blob/main/test_File.txt"  # Replace with a valid test file URL
upload_file = None  # Replace with a file path for upload speed testing
measure_speed(test_url, upload_file)
