<html>

<head>
  <title>Zodiac</title>
  
  <style type="text/css">
    body
    {
      background-color: blue;
    }
    h1
    {
      color: yellow;
      text-align: center;
      text-size: 40px;
      font-family: fantasy;
    }
    p
    {
      color: yellow;
      text-align: center;
      font-family: fantasy;
    }
    #formulari
    {
      position:absolute;
      top: 180px;
      left: 480px;
    }
    #pictures
    {
      position:absolute;
      left: 320px;
    }
  </style>
</head>
 
<body>
    <h1>Zodiac</h1>
    
    <div id="pictures">
    % for im in range(pictures):
    <img src="../static/${img[im]}" width="50px" heigh="50px"/>
    % endfor
    <p>Introdueix la data de naixement (aaaa-mm-dd) Descobreix el teu signe del zodiac</p>
    </div>
    <div id=formulari>
    <form method="post" action="/resultat">
      <input type="text" name="fecha">
      <input type="submit" value="Envia la data">
    </form>
    </div>
</body>
 
</html>
