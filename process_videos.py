import glob
import os
import subprocess
from concurrent.futures import ThreadPoolExecutor

python_file = r"scripts/demo_inference.py"
video_folder = r"" #path to video directory 
config_file = r"configs/coco/resnet/256x192_res152_lr1e-3_1x-duc.yaml"
checkpoint = r"model_files/fast_421_res152_256x192.pth"
output_dir = r"" #path to output directory

video_files = glob.glob(os.path.join(video_folder, "*.*"))

def check_file_processed(video_path):
    video_name = os.path.splitext(os.path.basename(video_path))[0]
    output_json_path = os.path.join(output_dir, f"alphapose-results-{video_name}.json")
    return os.path.exists(output_json_path)


def process_video(video_path, save_video = False):
    if video_path.lower().endswith(('.mp4', '.avi', '.mov')):
        if check_file_processed(video_path):
            print(f"Skipping: {video_path} (already processed)")
            return
            
        print(f'processing: {video_path}')
        command = [
            'python', python_file,
            '--cfg', config_file,
            '--checkpoint', checkpoint,
            '--video', video_path,
            '--outdir', output_dir,
            '--vis_fast'
        ]

        subprocess.run(command)
        print(f"Finished processing: {video_path}")

def delete_video(video_path):
    if not check_file_processed(video_path):
        command = ['rm', video_path]
        subprocess.run(command)
        print(f"deleting: {video_path}")

with ThreadPoolExecutor(max_workers = 1) as executor:
    executor.map(process_video, video_files)

print('Videos processed!')
