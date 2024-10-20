## CSV 2 TRIG Transformation

### (1) Jam your RDF into a CSV file for this example. 

<table>
<tr><b>
    <td>Column Name</td>
    <td>Usage</td>
</b></tr>
<tr>
  <td>graph_uri</td>
  <td>Named Graph URI with or without the enclosing &lt; &gt; </td>
</tr>
<tr>
  <td>subject_uri</td>
  <td>Object URI with or without the enclosing &lt; &gt; </td>
</tr>
<tr>
  <td>property_uri</td>
  <td>Predicate URI with or without the enclosing &lt; &gt; </td>
</tr>
<tr>
  <td>object_uri_or_literal_indicator</td>
  <td>
    <table>
    <tr>
      <td>Object URI with or without the enclosing &lt; &gt; </td>
    </tr>
    <tr>
      <td>L to indicate a literal</td>
    </tr>    
    </table>
  </td>
</tr>
  <tr>
  <td>literal_value</td>
  <td>quotes are not necessary</td>
</tr>
  <tr>
  <td>literal_datatype_uri</td>
  <td>URI in the xsd namespace</td>
</tr>
  <tr>
  <td>literal_language</td>
  <td>language bigraph if needed</td>
</tr>
</table>

### (2) Call the script:
```python csv_2_trig.py kennedys.csv```

### (3) Crack open the .trig file to view the quads.
<a href="https://github.com/johngugliotti/semanticwebpgm/blob/main/csv_to_trig_prototype/kennedys.trig">kennedys.trig</a>

