
import os

def apply_patch():
    motor_file = "/opt/render/project/src/.venv/lib/python3.11/site-packages/motor/frameworks/asyncio/__init__.py"
    if os.path.exists(motor_file):
        with open(motor_file, 'r') as file:
            content = file.readlines()

        new_content = []
        for line in content:
            if 'from asyncio import coroutine' in line:
                # Comment out the line that imports 'coroutine'
                new_content.append('# ' + line)
            else:
                new_content.append(line.replace('@coroutine', 'async def'))

        with open(motor_file, 'w') as file:
            file.writelines(new_content)

if __name__ == '__main__':
    apply_patch()