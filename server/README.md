# Overview

Project step 1 for Purdue ECE 30861 - Software Engineering

Team Members:\
Yi-Hsiang (Sean) Chang\
Connor Barry\
Erik Hays\
Seth Karner

## Project Description

This application is based upon a real-world scenario, prompted to us in ECE 30861 - Software Engineering at Purdue University. The task requires us to act as subcontractors for the ACME Corporation, recently one of their back-end components were ported to Node.js. Based upon success of this service, they want to bring up new Node.js-based services. As the team that provides infrastructure for the ACME Corp. we are tasked with making it easier for the services teams to get up and running.

## Service Description

The service will be prompted with a list of npm modules to grade. The service will then grade each module and return the results to the user in NDJSON format in the console. The grading will be based upon the following criteria:

- Ramp-up Time -> The ramp up time is mesaured by the readme file and how helpful it is for the user to get started using the module.

- Correctness -> The correctness of the module is determined by the number of open issues relative to the number of forks on the module. If the module has 100 issues but 10k forks, it may be a good module, but if it has 100 issues and 100 forks, it is likely a bad module with errors being found more commonly by less people.

- Bus Factor -> The bus factor is determined by the number of dependencies the module uses. If the module uses a ton of dependencies, it is likely that if one of those dependencies is abandoned, the module will be harder to maintain.

- Responsiveness -> The responsiveness of the module is determine by the time to close an issue as well as the time in between commits. The less time for each, the better the score. The time between commits is scaled by how long ago the most recent commit was.

- License Compatibility -> The license compatibility is determined by the license of the module. If the license is not compatible with the ACME Corp. the module will be given a score of 0.

These criteria will be graded on a scale of 0-1 with 1 being the best score. The total score will be calculated by an equation determined from the importance of each metric to the ACME Corpm and seen below:

(RAMPUP_SCORE \* 0.25 + CORRECTNESS_SCORE \* 0.2 + BUS_FACTOR_SCORE \* 0.15 + RESPONSIVENESS_SCORE \* 0.4) \* LICENSE_SCORE

This was deemed a good way to weight the metrics based upon the importance of each metric to the ACME Corp. The license score ultimately determines if the module is compatible with the ACME Corp. and is therefore the most important metric, if the license is not compatible the total score will be 0, resulting in an incompatible module.

## Getting Started

The command line interface supports the following commands:

- `install` - Installs the necessary dependencies for the application to function
- `build` - Builds the application and services. This is required before running the application
- `test` - Runs the test suite
- `url-file` - This is the path to a file containing a list of URLs to grade (one per line)

### To run these commands, input the following into the command line

```bash
./run <command>
```
