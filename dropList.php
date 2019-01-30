<?php
unlink('links.txt');
fopen("links.txt", "w");
header("Location: index.html");
?>