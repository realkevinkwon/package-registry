#[cfg(test)]


mod tests {
    use std::process::Command;
    // use pyo3::types::{IntoPyDict, PyModule};
    // use pyo3::prelude::*;
    // use dotenv;
    use std::io::{self, prelude::*, BufReader};
    use std::fs::File;
    use std::path::PathBuf;

    #[test]
    fn url_parsing() {
        let file1 = "sample/test_url/testurl_1.txt";
        let file2 = "sample/test_url/testurl_2.txt";

        // call python script to parse the url
        Command::new("python3")
            .arg("src/inputs/commands/valid_url.py")
            .arg(file1)
            .arg("output1.txt")
            .spawn()
            .expect("failed to execute process");

        Command::new("python3")
            .arg("src/inputs/commands/valid_url.py")
            .arg(file2)
            .arg("output2.txt")
            .spawn()
            .expect("failed to execute process");

        // check if the output is correct from sample/test_url/resulturl files
        let mut result1 = "sample/test_url/resulturl_1.txt";
        let mut result2 = "sample/test_url/resulturl_2.txt";
    }

    #[test]
    fn test_responsive() {
        // call python script to check responsiveness 

        /* we loop through the list of api url from sample/test_url to test*/
        let filepath = PathBuf::from("src/testurl.txt");

        // json path
        let jsonpath = PathBuf::from("src/inputs/commands/metrics.json");

        // Open the file in read-only mode (ignoring errors).
        let file = File::open(filepath).unwrap();
        // Create a buffered reader on the file.
        let reader = BufReader::new(file);

        for line in reader.lines() {
            let url = line.unwrap();
            // call python script to check licenses with url as argument
            Command::new("python3")
                .arg("src/inputs/commands/responsive.py")
                .arg(url.clone())
                .arg(jsonpath.clone())
                .output()
                .expect("failed to execute process");
        }
    }

    #[test]
    fn test_rampup() {
        // call python script to check rampup 

        /* we loop through the list of api url from sample/test_url to test*/
        let filepath = PathBuf::from("src/testurl.txt");

        // json path
        let jsonpath = PathBuf::from("src/inputs/commands/metrics.json");
        
        // Open the file in read-only mode (ignoring errors).
        let file = File::open(filepath).unwrap();
        // Create a buffered reader on the file.
        let reader = BufReader::new(file);

        for line in reader.lines() {
            let url = line.unwrap();
            // call python script to check licenses with url as argument
            Command::new("python3")
                .arg("src/inputs/commands/rampup.py")
                .arg(url.clone())
                .arg(jsonpath.clone())
                .output()
                .expect("failed to execute process");
            
            // grab the repo name from the url
            let repo_name = url.split("/").last().unwrap();

            // remove the cloned repo
            Command::new("rm")
                .arg("-rf")
                .arg(repo_name)
                .spawn()
                .expect("failed to execute process");
        }
    }

    #[test]
    fn test_correctness() {
        // call python script to check correctness

        /* we loop through the list of api url from sample/test_url to test*/
        let filepath = PathBuf::from("src/testurl.txt");

        // json path
        let jsonpath = PathBuf::from("src/inputs/commands/metrics.json");
        
        // Open the file in read-only mode (ignoring errors).
        let file = File::open(filepath).unwrap();
        // Create a buffered reader on the file.
        let reader = BufReader::new(file);

        for line in reader.lines() {
            let url = line.unwrap();
            // call python script to check licenses with url as argument
            Command::new("python3")
                .arg("src/inputs/commands/correctness.py")
                .arg(url.clone())
                .arg(jsonpath.clone())
                .output()
                .expect("failed to execute process");
        }
    }

    #[test]
    fn test_licenses() {
        /* call python script to check licenses */

        /* we loop through the list of api url from sample/test_url to test*/
        let filepath = PathBuf::from("src/testurl.txt");

        // json path
        let jsonpath = PathBuf::from("src/inputs/commands/metrics.json");
        
        // Open the file in read-only mode (ignoring errors).
        let file = File::open(filepath).unwrap();
        // Create a buffered reader on the file.
        let reader = BufReader::new(file);

        for line in reader.lines() {
            let url = line.unwrap();
            // call python script to check licenses with url as argument
            Command::new("python3")
                .arg("src/inputs/commands/metric_license.py")
                .arg(url.clone())
                .arg(jsonpath.clone())
                .output()
                .expect("failed to execute process");
        }
    }

    #[test]
    fn test_busfactor() {
        // call python script to check busfactor

        /* we loop through the list of api url from sample/test_url to test*/
        let filepath = PathBuf::from("src/testurl.txt");

        // json path
        let jsonpath = PathBuf::from("src/inputs/commands/metrics.json");
        
        // Open the file in read-only mode (ignoring errors).
        let file = File::open(filepath).unwrap();
        // Create a buffered reader on the file.
        let reader = BufReader::new(file);

        for line in reader.lines() {
            let url = line.unwrap();
            // call python script to check licenses with url as argument
            Command::new("python3")
                .arg("src/inputs/commands/metric_busfactor.py")
                .arg(url.clone())
                .arg(jsonpath.clone())
                .output()
                .expect("failed to execute process");
        }
    }

    // #[test]
    // fn test_popularity() {
    //     // load github token from env with dotenv
    //     dotenv::dotenv().ok();
    //     let mut token = std::env::var("GITHUB_TOKEN").expect("GITHUB_TOKEN must be set in your .env file");
    //     token = token.to_string();

    //     /* we loop through the list of api url from sample/test_url to test*/
    //     let filepath = PathBuf::from("src/resulturl.txt");
        
    //     // Open the file in read-only mode (ignoring errors).
    //     let file = File::open(filepath).unwrap();
    //     // Create a buffered reader on the file.
    //     let reader = BufReader::new(file);

    //     // create python file
    //     let py_popularity = include_str!("inputs/commands/popularity.py");

    //     pyo3::prepare_freethreaded_python();
    //     let gil = Python::acquire_gil();
    //     let py = gil.python();
    //     let py_module = PyModule::from_code(py, py_popularity, "popularity.py", "popularity").unwrap();
    //     let get_popularity_score_fn = py_module.getattr("get_popularity_score").unwrap();

    //     /* for each url in the file, we call the python script to test the popularity */
    //     for line in reader.lines() {
    //         // the function needs url = str, token = str
    //         let url = line.unwrap();
    //         let args = (url.clone(), token.clone());
    //         let popularity_score = get_popularity_score_fn.call1(args).unwrap().extract::<f64>().unwrap();
    //         println!("Tesing url: {}", url);
    //         println!("popularity score: {}", popularity_score);
    //     }
    // }

    fn test_metrics() {
        // check metrics
    }
}
