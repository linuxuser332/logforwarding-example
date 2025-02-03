A simple role to add the following to a server:

- Configure rsyslog to bind to a socket file
- A small python program to write data to the socket file
- Log data then forwarded by rsyslog to a Promtail container
- Promtail configured to forward to the data to a Loki (Grafan) instance
- The log data can be seen in the web UI

The point of this is just to prove, and to record that log data being written to a 
socket file can be forwarded to Loki.  Rsyslog can also dual route that data to 
other log destinations. 


