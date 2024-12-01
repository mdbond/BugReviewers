# BugReviewers

Mike Bond (Ohio State University)

### Overview

Generates e-mails to delinquent HotCRP reviewers.

### Before running the script

The script assumes that `submissions.html` and `pc.html` exist in current directory:

* `submissions.html` is a saved copy of a HotCRP paper search result such as [https://asplos25fall.hotcrp.com/search?q=%23vc.mike+show%3Areviewers&t=s](https://asplos25fall.hotcrp.com/search?q=%23vc.mike+show%3Areviewers&t=s). **Make sure the reviewers' names are visible before saving. If they're not visible, check the "Reviewers" box on the "View Options" tab.**

* `pc.html` is a saved copy of a PC page with e-mails such as [https://asplos25fall.hotcrp.com/users/pc](https://asplos25fall.hotcrp.com/users/pc).

Important: You'll need to edit `gen.py` to match your use case. At a minimum, change the signature (unless your name is also Mike) and the "From" e-mail.

### Running the script

```
rm -f *.eml # Remove previously generated .eml files to avoid confusing old and new .eml files
python3 gen.py
```

It writes e-mails in two formats:
* `.eml` files to the current directory
* plaintext to the terminal

### How to use `.eml` files

If your mailer doesn't support importing `.eml` files (e.g., if you're using the Outlook web app because you wisely chose Linux but your institution foolishly chose Outlook), you can try setting up Evolution to connect to your mail account, then copy the `.eml` files to the local Outbox folder, allowing a bulk send from Evolution:
```
cp *.eml ~/.local/share/evolution/mail/local/.Outbox/new/.
```

### Acknowledgments

Thanks to ChatGPT for generating most of the script.

Thanks to the ASPLOS 2025 reviewers for motivating the creation of this script by being delinquent in such large numbers.

### Disclaimer

Hasn't been tested outside of ASPLOS 2025 HotCRPs. Check the script's generated e-mails before sending them!

Improvements appreciated. Complaints not so much.
