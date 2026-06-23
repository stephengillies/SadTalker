import os
import sys

print("Python", sys.version)
print("Commit hash: docker-cu128-low-vram")
print("Skipping runtime requirements install; using baked image dependencies")
print("Launching SadTalker Web UI")


def start():
    from app_sadtalker import sadtalker_demo

    demo = sadtalker_demo()
    demo.launch(
        server_name=os.environ.get("GRADIO_SERVER_NAME", "0.0.0.0"),
        server_port=int(os.environ.get("GRADIO_SERVER_PORT", "7860")),
        share=False,
    )


if __name__ == "__main__":
    start()
