import os
from pathlib import Path
from dotenv import load_dotenv
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import PromptAgentDefinition

# Load environment variables from .env file
load_dotenv()

# Read instructions from prompt file
# prompt_file = Path(__file__).parent / 'prompts' / 'v1_instructions.txt'

    prompt_file = Path(__file__).parent / 'prompts' / 'v2_instructions.txt'
    ```

1. []Run the agent creation script:

     ```powershell
     python trail_guide_agent.py
     ```

    You should see output confirming the agent was created:

    ```
    Agent created (id: agent_yyy, name: trail-guide, version: 2)
    ```

    Note the Agent ID for later use.

1. []Commit your changes and tag the version:

    ```powershell
    git add trail_guide_agent.py
    git commit -m "Deploy trail guide agent V2 with enhanced capabilities"
    git tag v2
    ```

### Deploy trail guide agent V3

Finally, deploy the third version with production-ready features.

1. []Open `trail_guide_agent.py` and update the prompt file path:

   Change:

with open(prompt_file, 'r') as f:
    instructions = f.read().strip()
  
project_client = AIProjectClient(
    endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    credential=DefaultAzureCredential(),
)

agent = project_client.agents.create_version(
    agent_name=os.environ["AGENT_NAME"],
    definition=PromptAgentDefinition(
        model=os.getenv("MODEL_NAME", "gpt-5.1"),  # Use Global Standard model
        instructions=instructions,
    ),
)
print(f"Agent created (id: {agent.id}, name: {agent.name}, version: {agent.version})")