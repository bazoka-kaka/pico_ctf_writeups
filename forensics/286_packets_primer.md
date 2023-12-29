# Packets Primer

https://play.picoctf.org/practice/challenge/286

1. Download the packet capture

2. Open with wireshark

  <img src="../assets/286/286_1.png" />

3. Filter ARP protocols bc they're just messages relating IP and MAC addresses

   ```
   !arp
   ```

    <img src="../assets/286/286_2.png" />

4. Check the TCP packet's data containing <code>[PSH, ACK]</code> bc PSH means there's a data inside

  <img src="../assets/286/286_3.png" />

5. Get the flag

  <img src="../assets/286/286_4.png" />
