# BugReviewers

### Overview

Generates e-mails to delinquent HotCRP reviewers.

Important: You'll need to edit `gen.py` to match your use case.

### Inputs

The  `submissions.html` and `pc.html` exist in current directory:

* `submissions.html` is a saved copy of a HotCRP paper search result such as [https://asplos25summer.hotcrp.com/search?q=%23vc.mike+%23r2+&t=s](this). **You need to select "Reviewers" under "View Options" so that reviewer names are in the generated HTML**.

* `pc.html` is a saved copy of a PC page with e-mails such as [https://asplos25summer.hotcrp.com/users/pc](this).

### Outputs

Writes e-mails in two formats: .eml files and plaintext to the terminal.

### Acknowledgments

Thanks to ChatGPT for generating most of the text.

Thanks to the ASPLOS 2025 reviewers for being delinquent enough in their reviews in such large numbers as to justify making this script.

### Disclaimer

This is super untested. Improvements appreciated. Complaints not so much.
