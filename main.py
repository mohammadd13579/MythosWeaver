"""
MythosWeaver Runner
This is the main entry point to run the mythology generator.
It imports the Pantheon class, creates an instance,
populates it, and displays the result.
"""

from mythos_weaver import Pantheon

def main():
    """
    Main function to generate and display a new mythology.
    """
    
    # You can change the name of your pantheon here
    pantheon_name = "the Whispering Stars"
    
    # You can change the total number of gods to generate
    # (Must be 2 or more)
    num_gods = 9
    
    # 1. Create the pantheon
    my_mythology = Pantheon(pantheon_name)
    
    # 2. Populate it with gods and establish relationships
    my_mythology.populate(num_gods)
    
    # 3. Generate the creation myth based on the primordials
    myth = my_mythology.generate_creation_myth()
    print(myth)
    
    # 4. Display the full pantheon details
    my_mythology.display_pantheon()


if __name__ == "__main__":
    main()
