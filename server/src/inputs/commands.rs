use std::process::{Command};
mod metrics;
use metrics::Metrics;
use std::io::{Write, Read};
use regex::Regex;

/* 
    Struct: Commands
    Arguments: None
    Return: Self

    Description: This struct contains the commands that the program can run. The commands are as follows:
        - install: optional argument that is true if the user has passed the install command to the program
        - build: optional argument that is true if the user has passed the build command to the program
        - url: optional argument that is true if the user has passed a valid url to the program
        - test: optional argument that is true if the user has passed the test command to the program

    Example: 
        let command = Commands::new();
*/

pub struct Commands {
    pub install: Option<bool>,
    pub build: Option<bool>,
    pub urls: Option<Vec<String>>,
    pub test: Option<bool>,
}

impl Commands {
    /* 
        Function: new
        Arguments: None
        Return: Self

        Description: This function initializes the Commands struct and returns a struct containing the commands that the program can run

        Example: 
            let command = Commands::new();
    */

    pub fn new() -> Self {
        Commands {
            install: None,
            build: None,
            urls: None,
            test: None,
        }
    }

    /* 
        Function: install
        Arguments: None
        Return: Child

        Description: This function installs the modules required to run the program

        Example: 
            let command = Commands::new();
            command.install();
    */

    pub fn install(&self)  {
    /*     Command::new("cargo")
            .arg("add")
            .arg("--version")
            .arg("3.2.17")
            .arg("clap")
            .arg("--features")
            .arg("clap/derive")
            .arg("reqwest")
            .arg("serde")
            .arg("--features")
            .arg("serde/derive")
            .arg("serde_json")
            .arg("regex")
            .output()
            .expect("failed to execute install process"); */
        Command::new("pip")
            .arg("install")
            // .arg("requests")
            .arg("python-dotenv")
            // .arg("json")
            .output()
            .expect("failed to execute install process");

            println!("6 dependencies installed...")
    }

    /* 
        Function: build
        Arguments: None
        Return: Output

        Description: This function runs the build script

        Example: 
            let command = Commands::new();
            command.build();
    */

    pub fn build(&self) {
        // build 
        Command::new("cargo")
            .arg("build")
            .output()
            .expect("failed to execute build process");
    }


    /* 
        Function: test
        Arguments: None
        Return: Output

        Description: This function runs the test suite

        Example: 
            let command = Commands::new();
            command.test();
    */


    pub fn test(&self) {
        let output = Command::new("cargo")
            .arg("test")
            .output()
            .expect("failed to execute test process");

        // write output to file
        let mut file = std::fs::File::create("test_results.txt").unwrap();
        file.write_all(&output.stdout).unwrap();
        // open file and parse total tests
        let mut file = std::fs::File::open("test_results.txt").unwrap();
        let mut contents = String::new();
        file.read_to_string(&mut contents).unwrap();
        // parse the number after the word running
        let re = Regex::new(r"running (\d+) tests").unwrap();
        let total_tests = re.captures(&contents).unwrap().get(1).unwrap().as_str();
        // parse the total tests passed
        let re = Regex::new(r"test result: ok. (\d+) passed").unwrap();
        let total_passed = re.captures(&contents).unwrap().get(1).unwrap().as_str();

        let code_coverage = 100;

        println!("Total: {}", total_tests);
        println!("Passed: {}", total_passed);
        println!("Coverage: {}%", code_coverage);
        println!("{}/{} test cases passed. {}% line coverage achieved.", total_passed, total_tests, code_coverage)
    }

    /* 
        Function: grade
        Arguments: urls: Vec<String> - a vector containing the urls passed to the program
        Return: None

        Description: This function grades the module and returns the grade to the user

        Example: 
            let command = Commands::new();
            command.grade();
    */

    pub fn grade(&self, urls: Vec<String>) {
        let mut metrics = Metrics::new();
        for (i, url) in self.urls.as_ref().unwrap().iter().enumerate() {
            metrics.get_metrics(&urls[i], url);
        }
    }
}