use clap::Parser;
use std::fs;
use regex::Regex;

pub mod commands;
use commands::Commands;


/* 
    Struct to parse the arguments passed to the program using clap
    This struct uses the clap syntax found at https://docs.rs/clap/latest/clap/
*/

#[derive(Parser, Debug)]
#[clap(author,version,about,long_about=None)]
pub struct Args {
    /// The command to execute
    #[clap(short, long, value_parser)]
    pub command: String,
}

impl Args {
    /* 
        Function: new
        Arguments: None
        Return: Self

        Description: This function parses the arguments passed to the program using clap and returns a struct containing the arguments passed to the program

        Example: 
            let args = Args::new();
    */
    
    pub fn new() -> Self {
        Args::parse()
    }


    /* 
        Function: parse_commands
        Arguments: None  - requires the struct to be initialized
        Return: None

        Description: This function parses the commands passed to the program and runs the appropriate command
            - install: installs the modules required to run the program
            - build: runs the build script
            - test: runs the test suite
            - _: checks to see if the url passed to the program is a valid url and if it is, it grades the module and returns the grade to the user. If the url is not valid, it calls the {invalid args} function and returns an error message to the user

        Example: 
            let args = Args::new();
            args.parse_commands();
    */

    pub fn parse_commands(&self) {
        let mut command = Commands::new();
        match self.command.as_str() {
            "install" => {
                command.install = Some(true);
                command.install();
            },
            "build" => {
                command.build = Some(true);
                command.build();
            },
            "test" => {
                command.test = Some(true);
                command.test();
            },  
            _ => {
                self.get_file_urls();
            },
        }
    }

    /* 
        Function: get_file_urls
        Arguments: path - the path to the file containing the urls
        Return: Vec<String> - a vector containing the urls

        Description: This function reads the file containing the urls and returns a vector containing the urls, it also checks if these are valid github/npm urls

        Example: 
            let args = Args::new();
            args.parse_commands;

            -- depending on the command being paresed, determines if this function is called. NOT called directly by user
    */

    fn get_file_urls(&self)  {   
        let path = self.command.as_str();
        let contents = fs::read_to_string(path).expect("Something went wrong reading the file");
        let mut urls: Vec<String> = contents.split_whitespace().map(|s| s.to_string()).collect();
        let original_urls: Vec<String> = urls.clone();
        let mut temp_urls: Vec<String> = Vec::new();
        let re = Regex::new(r"https://(github.com|www.npmjs.com)/[a-zA-Z0-9_-]+/[a-zA-Z0-9_-]+").unwrap();

        for url in urls.iter() {
            let mut s = String::from(url);
            if re.is_match(url) {
                if url.contains("github.com") {
                    if url.contains("www.") {
                        s = s.replace("www.github.com", "api.github.com/repos")
                    }
                    else {
                        s = s.replace("github.com", "api.github.com/repos")
                    }
                }
                
                if url.contains("npmjs.com") {
                    if url.contains("www.") {
                        s = s.replace("www.npmjs.com", "registry.npmjs.org");
                        s = s.replace("package/", "");
                    }
                    else {
                        s = s.replace("npmjs.com", "registry.npmjs.org");
                        s = s.replace("package/", "");
                    }
                }

                temp_urls.push(s.to_string());
            }
            else {
                println!("{} is not a valid url", url);
            }
        }
        urls = temp_urls;

        let mut command = Commands::new();
        command.urls = Some(urls);
        command.grade(original_urls);
    }

}
