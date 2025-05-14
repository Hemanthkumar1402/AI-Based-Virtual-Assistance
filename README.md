PROJECT TITLE:
AI BASED VIRTUAL ASSISTANCE FOR INTELLIGENT TASK AUTOMATION

PROBLEM STATEMENT:
  With the increasing reliance on digital interfaces, users need quick access to tools like reminders, search, app launchers, and general information. Most assistants either require a UI or Internet connection and fail to run natively and privately on a system.
  There is a need for a lightweight, command-line based virtual assistant that can understand natural language commands, answer questions, and control local and online apps — all from one interface.

PROPOSED SOLUTION:
  We propose a Python-based AI Virtual Assistant that understands user inputs via natural language processing (NLP), detects user intent, and performs actions such as:
  1.Telling time
  2.Setting reminders
  3.Fetching answers from Wikipedia
  4.Performing calculations
  5.Opening social media or desktop apps
  6.Answering general queries

ALGORITHM LOGIC:
  1.Intent Detection: Match user text against known command types using keyword matching and regular expressions
  2.Action Routing: Based on intent, call the appropriate function
  3.General Questions: Use Wikipedia to return concise answers
  4.App Launching: Use webbrowser or os.system to open applications  
