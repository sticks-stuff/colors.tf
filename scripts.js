// return JSON data from any file path (asynchronous)
function getJSON(path) {
    return fetch(path).then(response => response.json());
}

document.getElementById('red').addEventListener("change", watchColorPickerRed, false);
document.getElementById('blue').addEventListener("change", watchColorPickerBlue, false);

function watchColorPickerRed(event) {
    watchColorPicker(event, "red")
}

function watchColorPickerBlue(event) {
    watchColorPicker(event, "blue")
}

function watchColorPicker(event, team) {
	color = hexToRgb(event.target.value);
	
    if(team == "red") {
        originalHSL = rgbToHsl(255, 0, 24); //god i love hard coding vars
    } else {
        originalHSL = rgbToHsl(0, 30, 255);
    }

	colorHSL = rgbToHsl(color[0], color[1], color[2])
	var newColorDiff = [];
	newColorDiff[0] = colorHSL[0] - originalHSL[0];
	newColorDiff[1] = colorHSL[1] - originalHSL[1];
	newColorDiff[2] = colorHSL[2] - originalHSL[2];
	console.log({originalHSL})
	console.log({colorHSL})
	console.log({newColorDiff})
	Array.from(document.getElementsByClassName(`${team}-particle`)).forEach(element => {
		Array.from(element.getElementsByClassName('colour-display')).forEach(element => {
			originalColor = element.attributes.ogcolour.value;
			// originalColor = originalColor.slice(10, -1);
            // console.log(originalColor)
			originalColor = originalColor.split(' ');
			originalColorHSL = rgbToHsl(originalColor[0], originalColor[1], originalColor[2]);
			console.log({originalColorHSL})
			originalColorHSL[0] += newColorDiff[0];
			originalColorHSL[1] += newColorDiff[1];
			originalColorHSL[2] += newColorDiff[2];
			originalColor = hslToRgb(originalColorHSL[0], originalColorHSL[1], originalColorHSL[2]);
			element.style.backgroundColor = 'rgb(' + originalColor.join(', ') + ')';
		});
	});
}

function hexToRgb(hex) {
	var result = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hex);
	if(result){
		var r= parseInt(result[1], 16);
		var g= parseInt(result[2], 16);
		var b= parseInt(result[3], 16);
		return [r, g, b];
	} 
	return null;
}

/**
 * Converts an HSL color value to RGB. Conversion formula
 * adapted from http://en.wikipedia.org/wiki/HSL_color_space.
 * Assumes h, s, and l are contained in the set [0, 1] and
 * returns r, g, and b in the set [0, 255].
 *
 * @param   {number}  h       The hue
 * @param   {number}  s       The saturation
 * @param   {number}  l       The lightness
 * @return  {Array}           The RGB representation
 */
 function hslToRgb(h, s, l){
    var r, g, b;

    if(s == 0){
        r = g = b = l; // achromatic
    }else{
        var hue2rgb = function hue2rgb(p, q, t){
            if(t < 0) t += 1;
            if(t > 1) t -= 1;
            if(t < 1/6) return p + (q - p) * 6 * t;
            if(t < 1/2) return q;
            if(t < 2/3) return p + (q - p) * (2/3 - t) * 6;
            return p;
        }

        var q = l < 0.5 ? l * (1 + s) : l + s - l * s;
        var p = 2 * l - q;
        r = hue2rgb(p, q, h + 1/3);
        g = hue2rgb(p, q, h);
        b = hue2rgb(p, q, h - 1/3);
    }

    return [Math.round(r * 255), Math.round(g * 255), Math.round(b * 255)];
}

/**
 * Converts an RGB color value to HSL. Conversion formula
 * adapted from http://en.wikipedia.org/wiki/HSL_color_space.
 * Assumes r, g, and b are contained in the set [0, 255] and
 * returns h, s, and l in the set [0, 1].
 *
 * @param   {number}  r       The red color value
 * @param   {number}  g       The green color value
 * @param   {number}  b       The blue color value
 * @return  {Array}           The HSL representation
 */
 function rgbToHsl(r, g, b){
    r /= 255, g /= 255, b /= 255;
    var max = Math.max(r, g, b), min = Math.min(r, g, b);
    var h, s, l = (max + min) / 2;

    if(max == min){
        h = s = 0; // achromatic
    }else{
        var d = max - min;
        s = l > 0.5 ? d / (2 - max - min) : d / (max + min);
        switch(max){
            case r: h = (g - b) / d + (g < b ? 6 : 0); break;
            case g: h = (b - r) / d + 2; break;
            case b: h = (r - g) / d + 4; break;
        }
        h /= 6;
    }

    return [h, s, l];
}

function mod (n, m) {
    var remain = n % m;
    return Math.floor(remain >= 0 ? remain : remain + m);
}

function modifyJSON() {
    getJSON('output.json').then(data => {
        Array.from(document.getElementsByClassName('colour-display')).forEach(element => {
            jsonPath = element.attributes.jsonpath.value;
            jsonPath = jsonPath.split(',');
            jsonElement = data[jsonPath[0]][jsonPath[1]][jsonPath[2]];

            newColor = element.style.backgroundColor;
			newColor = newColor.substring(4).slice(0, -1);
			newColor = newColor.split(', ');

            jsonElement[0] = newColor[0];
            jsonElement[1] = newColor[1];
            jsonElement[2] = newColor[2];
        });
        console.log(data);
    })    
}