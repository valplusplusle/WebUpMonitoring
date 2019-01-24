<?php
//New Post
if ( $_POST['link'] <> "" )
{
	$handle = fopen ( "links.txt", "a" );		
   	//write from form in stream
	fwrite ( $handle, $_POST['link']);
	fwrite ( $handle, PHP_EOL);
	//close stream
	fclose ( $handle );	

    header("Location: index.html");
    // Datei wird nicht weiter ausgef?hrt
	exit;
}
?>
