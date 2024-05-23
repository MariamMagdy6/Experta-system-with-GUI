# Restaurant Expert System with GUI

This project is a restaurant expert system with a graphical user interface (GUI) developed using Tkinter and Experta. The system allows users to select menu items, view the bill, and confirm or cancel the billing process.

## Features

- **GUI with Tkinter**: User-friendly interface to select menu items and view the bill.
- **Expert System with Experta**: Handles the billing confirmation and cancellation processes.
- **Dynamic Bill Calculation**: Calculates the total bill based on selected items and their quantities.
- **Editable Bill**: Allows users to edit the quantities of selected items before confirming the bill.

## Requirements

- Python 3.x
- Tkinter
- Experta

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/restaurant-expert-system.git
    cd restaurant-expert-system
    ```

2. Install the required Python packages:
    ```bash
    pip install experta
    ```

## Usage

1. Run the main Python script:
    ```bash
    python main.py
    ```

2. Follow the prompt to decide whether to display the GUI:
    - Enter `yes` to display the GUI.
    - Enter `no` to exit the application.

3. Use the GUI to select menu items and enter quantities.

4. Click the "Check Bill" button to view the bill. You can then:
    - **Edit**: Edit the quantities of the selected items.
    - **Confirm**: Confirm the billing.
    - **Cancel**: Cancel the billing.

## Code Overview

### GUI Functions

- **calculate_bill(facts)**: Calculates the total bill based on the selected items and their quantities.
- **show_bill(facts)**: Displays the bill in a new window.
- **display_bill(total_bill, facts)**: Displays the detailed bill with options to edit, confirm, or cancel.
- **edit_quantity(bill_text, facts)**: Allows the user to edit the quantities of the selected items.

### Expert System with Experta

- **find_bill(KnowledgeEngine)**: Defines the expert system with rules for confirming, canceling, and editing the bill.
  - **confirm_billing**: Displays a confirmation message and closes the bill window.
  - **cancel_billing**: Displays a cancellation message and closes the bill window.
  - **edit_bill**: Handles the action after the bill is edited.

### Main Function

- **main()**: Initializes the GUI, defines menu items and their prices, and starts the expert system engine.

## Acknowledgements

- Tkinter for the GUI framework
- Experta for the rule-based expert system

