import schemdraw
from schemdraw.flow import *

def generate_flowchart():
    """Generates a flowchart and saves it as an image file."""
    with schemdraw.Drawing() as d:
        # Start point
        d += Start().label('Start')
        d += Arrow().down()
        
        # Process 1
        d += Box().label('Process 1: \nGet user input')
        d += Arrow().down()
        
        # Decision 1
        d += Decision().label('Decision 1: \nIs input valid?')
        d += Arrow().down().length(2)
        
        # Process 2
        d += Box().label('Process 2: \nProcess data')
        d += Arrow().down()
        
        # End
        d += End().label('End')
        
        # Save the flowchart
        d.save('flowchart.png')
        print("Flowchart saved as 'flowchart.png'")

def generate_transcript():
    """Generates a transcript (text description) of the flowchart steps."""
    transcript = (
        "Flowchart Steps:\n"
        "1. Start: The process begins.\n"
        "2. Process 1: Get user input from the system or user interface.\n"
        "3. Decision 1: Check if the input is valid. This is a decision point.\n"
        "    - If the input is valid, the process proceeds.\n"
        "    - If the input is not valid, the system may ask for input again or show an error.\n"
        "4. Process 2: Process the input data based on the logic or criteria.\n"
        "5. End: The process concludes.\n"
    )
    
    # Save the transcript to a text file
    with open('flowchart_transcript.txt', 'w') as f:
        f.write(transcript)
    
    print("Transcript saved as 'flowchart_transcript.txt'")

# Generate both the flowchart and the transcript
generate_flowchart()
generate_transcript()
