<html>
<head>
    <title>${project}</title>
</head>
 
<body>
    <h1>Projecte ${project}</h1>
    
    <table>
       <tr>
        % for picture in range(pictures):
           <td> <img src="../static/${picture}.png"> </td>
        % endfor
       </tr>
    </table>
<br/>
<br/>
    <a href="/zodiac">Ves al formulari</a>
</body>
 
</html>
