# ADK Demo: Google Framework

This project demonstrates the use of the [ADK (Agent Development Kit)](https://google.github.io/adk-docs/) within the context of Google's framework technologies. ADK is an open-source platform for building, deploying, and managing intelligent agents that can automate tasks, integrate with APIs, and interact with users or systems.

## What is ADK?

[ADK](https://google.github.io/adk-docs/) is a flexible, extensible framework for developing agent-based applications. It provides tools and libraries for creating agents that can reason, plan, and act autonomously or collaboratively. ADK supports integration with web services, cloud platforms, and custom workflows.

## Features

- **ADK Integration**: Example of using the Agent Development Kit with Google technologies.
- **Modular Architecture**: Easily extend and customize agents for various use cases.
- **Demo Agent**: Sample agent implementation for demonstration and testing.
- **Python-based**: Core agent logic implemented in Python.
- **Web UI**: Launch and manage agents using the ADK web interface.
- **API Integration**: Connect agents to external APIs and services.
- **Extensive Documentation**: See the [official ADK docs](https://google.github.io/adk-docs/) for more details.

## Getting Started

### Prerequisites

- Python 3.8+
- ADK (Agent Development Kit) installed ([installation guide](https://google.github.io/adk-docs/getting-started/installation/))

### Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/M97Chahboun/adk-demo.git
   cd adk-demo
   ```

2. (Optional) Set up a virtual environment:
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

4. Install ADK (if not already installed):
   ```sh
   pip install adk
   ```

### Running the Demo

To start the agent and launch the ADK web interface:
```sh
adk web
```
This will start the ADK server and open the web UI where you can manage and interact with your agents.

## Project Structure

- `multi_tool_agent/`: Contains the agent implementation and related modules.
- `README.md`: Project documentation.

## Contributing

Contributions are welcome! Please open issues or submit pull requests for improvements.

## License

This project is licensed under the MIT License.