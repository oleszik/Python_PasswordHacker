Password Hacker – Timing Attack Exploit
This Python program demonstrates a timing-based side-channel attack against a vulnerable authentication server. It was developed as part of the JetBrains Academy / Hyperskill "Password Hacker" project.

What It Does
Login Discovery:
The program iterates through a list of potential logins and identifies the correct one by checking the server's response.

Timing Attack on Password:
Using the known timing vulnerability, the program detects correct password characters one by one by measuring the server’s response time.
When a correct character is guessed, the server takes slightly longer to respond due to internal exception handling.

Persistent Connection:
For maximum efficiency and compatibility with the challenge environment, the program maintains a single socket connection throughout execution.

Features
Implements a real-world timing side-channel attack

Uses high-precision timers for reliable delay detection

Minimizes server load by avoiding unnecessary reconnections

Clean, readable, and ready for educational demos or CTF-style scenarios

You need a logins.txt file containing possible login names (included in the project).

Concepts Demonstrated
Socket programming in Python

JSON communication protocol

Brute-force logic

Timing-based vulnerability exploitation

Simple network pentesting techniques

