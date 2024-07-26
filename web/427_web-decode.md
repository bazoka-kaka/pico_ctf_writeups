# Web Decode

## Problem

Do you know how to use the web inspector? Start searching here to find the flag

## Solution

Go to about.html, inspect, then you'll see

```html
<section class="about" notify_true="cGljb0NURnt3ZWJfc3VjYzNzc2Z1bGx5X2QzYzBkZWRfMjgzZTYyZmV9">
    <h1>
    Try inspecting the page!! You might find it there
    </h1>
<!-- .about-container -->
</section>
```

there, you can decode the value of notify_true `echo cGljb0NURnt3ZWJfc3VjYzNzc2Z1bGx5X2QzYzBkZWRfMjgzZTYyZmV9 | base64 -d`

FLAG: `picoCTF{web_succ3ssfully_d3c0ded_283e62fe}`