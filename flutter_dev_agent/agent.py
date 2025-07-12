from google.adk.agents import Agent, LlmAgent
import subprocess



def run_command(command: str) -> dict:
    """Executes a shell command and returns the result.

    Args:
        command (str): The command to execute.

    Returns:
        dict: A dictionary containing the command output or error message.
    """
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return {
            "status": "success",
            "output": result.stdout,
            "error": result.stderr
        }
    except Exception as e:
        return {
            "status": "error",
            "error_message": str(e)
        }

def write_to_file(file_path: str, content: str) -> dict:
    """Writes content to a file, creating it if it doesn't exist.

    Args:
        file_path (str): Path to the file.
        content (str): Content to write.

    Returns:
        dict: Operation status and any error messages.
    """
    try:
        with open(file_path, 'w', encoding="utf-8") as f:
            f.write(content)
        return {"status": "success"}
    except Exception as e:
        return {"status": "error", "error_message": str(e)}

flutter_file_agent = Agent(
    name="flutter_file_agent",
    model="gemini-2.0-flash",
    description="A specialized agent for Flutter project file management and organization",
    instruction=(
        "You are a Flutter file management specialist that can:\n"
        "1. Read, Create, move, or delete project files and directories\n"
        "2. Organize project structure and assets\n"
        "3. Handle file permissions and access\n"
        "4. Manage resource files and assets\n"
        "5. Handle file encoding and format conversions\n"
        "6. Clear and write new content to files\n"
        "7. Create and update configuration files\n\n"
        "8. modify files on my computer. \n\n"
        "Maintain clean project organization and follow Flutter conventions."
    ),
    tools=[run_command, write_to_file]
)


# Flutter Project Setup Agent
flutter_setup_agent = Agent(
    name="flutter_setup_agent",
    model="gemini-2.0-flash",
    description="A specialized agent for setting up new Flutter projects and managing project configuration",
    instruction=(
        "You are a Flutter project setup specialist that can:\n"
        "1. Create new Flutter projects\n"
        "2. Set up development environments\n"
        "3. Configure platform-specific settings\n"
        "4. Manage dependencies in pubspec.yaml\n"
        "5. Initialize version control\n\n"
        "Always verify project requirements and provide clear setup instructions."
    ),
    tools=[run_command]
)

# Flutter Development Agent
flutter_dev_agent = Agent(
    name="flutter_dev_agent",
    model="gemini-2.0-flash",
    description="A specialized agent for Flutter development tasks and code generation",
    instruction=(
        "You are a Flutter development specialist that can:\n"
        "1. Generate Flutter widgets and screens\n"
        "2. Implement state management solutions\n"
        "3. Create responsive layouts\n"
        "4. Add platform-specific implementations\n"
        "5. Handle routing and navigation\n\n"
        "Focus on writing clean, maintainable code following Flutter best practices."
    ),
    tools=[run_command]
)

# Flutter Testing Agent
flutter_test_agent = Agent(
    name="flutter_test_agent",
    model="gemini-2.0-flash",
    description="A specialized agent for Flutter testing and quality assurance",
    instruction=(
        "You are a Flutter testing specialist that can:\n"
        "1. Run Flutter tests (unit, widget, integration)\n"
        "2. Generate test coverage reports\n"
        "3. Perform build validation\n"
        "4. Check code quality and lint issues\n"
        "5. Monitor app performance\n\n"
        "Ensure comprehensive test coverage and maintain code quality standards."
    ),
    tools=[run_command]
)

# Flutter Deployment Agent
flutter_deploy_agent = Agent(
    name="flutter_deploy_agent",
    model="gemini-2.0-flash",
    description="A specialized agent for Flutter app deployment and release management",
    instruction=(
        "You are a Flutter deployment specialist that can:\n"
        "1. Build release versions for different platforms\n"
        "2. Handle app signing and certificates\n"
        "3. Manage app store deployments\n"
        "4. Configure CI/CD pipelines\n"
        "5. Handle version management\n\n"
        "Follow platform-specific guidelines and security best practices."
    ),
    tools=[run_command]
)

root_agent = LlmAgent(
    name="flutter_orchestrator_agent",
    model="gemini-2.0-flash",
    description=(
        "A master agent that orchestrates Flutter application development by coordinating "
        "specialized sub-agents for project setup, development, testing, and deployment phases. "
        "It analyzes requirements and delegates tasks to the most appropriate sub-agent to "
        "ensure efficient and high-quality Flutter app development."
    ),
    sub_agents=[
        flutter_file_agent,
        flutter_setup_agent,
        flutter_dev_agent,
        flutter_test_agent,
        flutter_deploy_agent
    ]
)