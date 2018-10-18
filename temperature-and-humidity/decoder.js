function Decoder(bytes, port) {
  var result = "";
	for(var i = 0; i < bytes.length; ++i){
		result+= (String.fromCharCode(bytes[i]));
	}

	var data = result.split(" ");
  return {
    "temperature": data[0],
    "humidity": data[1]
  };
}
