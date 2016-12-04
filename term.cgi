#!/bin/bash
#Create by: David Christian Dias Ordone
#Cooperations by:

HELP="Bem vindo ao Terminal Remoto do Linux via browser\n
Você poderá executar um comando por vez\n
Não poderá ser feita a utilização de alguns operadores como o PIPE '|' e o operador diamente '>'\n
Se você souber solucionar está adversidade baixe o código no github\n
https://github.com/TurkojanOwnz/TerminalWeb.git"
COMMAND=`echo $QUERY_STRING | sed -e "s/^.*COMMAND=\([^&]*\)/\1/"`
LINHA="[`whoami` -> `pwd`]:"

cat <<EOF
Content-type: text/html

<html>
	<head>
        <style>
			body {
                background-color: #0c0a15;
			}
            .border {
				background-color: #696969;
                padding-right: 20px;
                padding-left: 20px;
                border-radius: 10px;
                border: 1px solid;
                box_shadow: 1px 1px 2px;
                *zoom: 1;
            }

            .border:before,
            .border:after {
                display: table;
                line-height: 0;
                padding-top: 5px;
                content: "";
            }

            .border:after {
                clear: both;
            }
			label {
				color: white;
				font-weight: bold;
				font-family: Sans-serif;
                font-size: 21px;
			}
			input[type="text"] {
				border-radius:4px;
				border:1px solid #000000;
				background: #ddd;
				box-shadow: 1px 1px 2px #333333;
                height: 26px;
				width: 60%;
				max-width: 75%;
			}
			input[type="submit"] {
				background-color:#006699;
        		color:#ffffff;
        		border-radius:4px;
        		border:1px solid #000000;
        		box-shadow: 1px 1px 2px #333333;
        		font-weight:bold;
                font-size: 20px;
                font-family: Sans-serif;
				height: 30px;
				width: 90px;
			}
			input[type=text]:hover{ 
         		background: #ffffff; border:1px solid #ff0000;
			}
			input[type="submit"]:hover{
				background: #4682B4; border:1px solid #ff0000;
			}
			textarea {
				background-color: #ddd;
				color: black;
				border: 1px solid #000000;
				border-radius:4px;
				box-shadow: 1px 1px 2px #333333;
				height: 87%;
				width: 100%;
			}
		</style>
		<title>Terminal Remoto</title>
	</head>
	<body>
        <div class="border">
        <form name='form_nome' method='GET' action='term.cgi'>
		<label>Comando: </label>
		<input type="text" size="30" name="COMMAND" maxlength="50"/>
		<input type="submit" value="Enviar" />
		<br>
		<br>
		<textarea readonly="readonly" style="resize:none;">
EOF

if [ -n "$COMMAND" ]; then
	RESULT=`echo -e $COMMAND | sed -e "s/+/ /g" | sed -e "s/%22/\"/g" | sed -e "s/%21/!/g" | sed -e "s/%40/@/g" | sed -e "s/%23/#/g" | sed -e "s/%24/$/g" | sed -e "s/%25/%/g" | sed -e "s/%26/\&/g" | sed -e "s/%28/(/g" | sed -e "s/%29/)/g" | sed -e "s/%3D/=/g" | sed -e "s/%2B/+/g" | sed -e "s/%2F/\//g" | sed -e "s/%3F/?/g" | sed -e "s/%27/'/g" | sed -e 's/%60/\`/g' | sed -e "s/%5B/[/g" | sed -e "s/%7B/{/g" | sed -e "s/%5E/^/g" | sed -e "s/%7E/~/g" | sed -e "s/%7D/}/g" | sed -e "s/%5D/]/g" | sed -e "s/%7C/|/g" | sed -e "s/%2C/,/g" | sed -e "s/%3C/</g" | sed -e "s/%3E/>/g" | sed -e "s/%3B/;/g" | sed -e "s/%3A/:/g"`
    echo -e "$LINHA $RESULT\n`$RESULT`"
else
	echo -e "$LINHA $HELP"
fi

echo -e "</textarea>\n</form>\n</div>\n</body>\n</html>"
