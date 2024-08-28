# BugReviewers

Mike Bond (Ohio State University)

### Overview

Generates e-mails to delinquent HotCRP reviewers.

### Before running the script

The script assumes that `submissions.html` and `pc.html` exist in current directory:

* `submissions.html` is a saved copy of a HotCRP paper search result such as [https://asplos25summer.hotcrp.com/search?q=%23vc.mike+%23r2+&t=s](this).

* `pc.html` is a saved copy of a PC page with e-mails such as [https://asplos25summer.hotcrp.com/users/pc](this).

Important: You'll need to edit `gen.py` to match your use case. At a minimum, change the signature (unless your name is also Mike) and the "From" e-mail.

### Running the script

```
python3 gen.py
```

It writes e-mails in two formats:
* `.eml` files to the current directory
* plaintext to the terminal.

As of 28 August 2024, the `.eml` files are untested since I don't have a client that supports them (for e-mail I use the Outlook web client).

### Acknowledgments

Thanks to ChatGPT for generating most of the script.

Thanks to the ASPLOS 2025 reviewers for being delinquent in such large numbers as to justify making this script.

### Disclaimer

This is super untested. Check its results when using it!

Improvements appreciated. Complaints not so much.
