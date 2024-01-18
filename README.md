# PreferenceMatcher

## Overview

PreferenceMatcher is a versatile algorithm designed to match individuals with similar preferences based on responses gathered through Google Forms. Whether you're looking for a compatible roommate, a book exchange partner, or a collaborator for a music project, PreferenceMatcher is here to streamline the process.

## How it Works

Each participant is represented as an array, with each dimension of the array corresponding to the option selected for a specific question. The key assumption is that the sequential order of options reflects the degree of preference, with option 'a' being closer to 'b' than 'c'. This sequential arrangement ensures that a person selecting options 'a', 'b', 'c', 'd' would be considered a closer match with someone who chose 'a', 'c', 'b', 'd' rather than 'a', 'b', 'j', 'd'.

## Example Usages

- **Roommate Matching:** Find the perfect roommate by aligning preferences for living arrangements, lifestyle choices, and more.
  
- **Book Exchange Matching:** Connect with individuals who share similar literary tastes, ensuring a more enjoyable book exchange experience.

- **Music Collaboration Connector:** Pair up with musicians whose musical preferences complement your own, enhancing the synergy in your collaborative projects.

## Requirements

To achieve accurate matching, it is crucial to organize the form options for every question in a sequential order of preference. This ensures the algorithm interprets the data accurately, enhancing the quality of matches.

## Getting Started

1. Clone the repository to your local machine.
2. Ensure that your Google Form options are arranged in a sequential order of preference for accurate matching.
3. Run the algorithm, providing the necessary input data.

## Contributing

We welcome contributions to enhance and expand the capabilities of PreferenceMatcher. Feel free to open issues, submit pull requests, or suggest new features to make this project even more powerful.

## License

PreferenceMatcher is released under the [MIT License](LICENSE).
