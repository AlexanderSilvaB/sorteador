<!-- 
  @Author: Alexander Silva Barbosa
  @Date:   2022-09-09 12:28:22
  @Last Modified by:   Alexander Silva Barbosa
  @Last Modified time: 2022-09-09 12:43:08
-->
<html>

<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>$TITLE</title>
</head>

<body>
    <h3 style="text-align: center;">$TITLE</h3>
    <hr/>
    <h2 style="text-align: center;">Você saiu com:</h2>
    <h1 id="name" style="text-align: center;"></h1>
    <br/>
    <br/>
    <p>$RESTRICTIONS</p>
    <script>
        var data = $DATA;
        if (window.location.hash && window.location.hash.length > 0) {
            var code = window.location.hash.replace('#', '');
            if (code in data)
                document.getElementById('name').innerText = data[code];
            else
                document.getElementById('name').innerText = "Ninguém";
        } else {
            document.getElementById('name').innerText = "Ninguém";
        }
    </script>
</body>

</html>