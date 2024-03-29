# iotobex-client-example-stomp-python

Example of client implementation demonstrating a method of connection to the Real Time Service, in this case a STOMP connection implemented in Python.

STOMP (Streaming Text Orientated Messaging Protocol) is a simple text-based protocol, designed for working with message-oriented middleware. It’s easy to implement the STOMP client in an arbitrary programming language, and is well suited to messaging from scripted applications in languages such as Ruby, Python, PHP, and Perl.

This code utilizes the Python STOMP client by Jason R Briggs, and has been tested using version 5.0.1. Be sure to add the stomp.py package to your project.

You will need an Real Time Service user account. Be sure to configure the credentials and access URL and port in ClientExampleStompPython.py as per the Credentials and STOMP specifics as provided through the Real Time Service POC Console. 

Note that the stream name utilized in the example must be configured for the user whose credentials are specified. To do this, configure the stream name as both a publishable and subscribed stream by means of the Real Time Service POC Console.
