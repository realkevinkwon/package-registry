mod inputs;
use inputs::Args;
use inputs::commands::Commands;
use std::env;


fn main() {
    // initialize a list of arguments passed to the program in the case that the user does not have clap installed
    let initial_args: Vec<String> = env::args().collect();

    // This is a check to make sure the user has passed the correct number of arguments to the service
    // the program panics if the user has not passed the correct number of arguments
    if initial_args.len() < 2 {
        panic!("Not enough arguments were passed"); // print an error message to console
    }

    /* 
        This is a check to see if the user has passed the install command to the program
        if the user has passed the install command, the program will install the clap crate and any other dependencies    
    */
    else if initial_args.len() == 3 && initial_args[2] == "install" {
        let mut command = Commands::new();
        command.install = Some(true);
        command.install();
    } 
    /*  
        This acknowledges that the user has passed the correct number of arguments to the program and knows the user has clap installed, so the program will parse the commands using clap and run the appropriate command
    */

    else {
        let args = Args::new();
        args.parse_commands();
    }
    
}