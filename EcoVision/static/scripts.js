const socket = io.connect('http://' + document.domain + ':' + location.port);

socket.on('classification', function(data) {
    const classificationText = document.getElementById('classification');
    classificationText.textContent = data.text;
});

(function(d, t) {
    var v = d.createElement(t), s = d.getElementsByTagName(t)[0];
    v.onload = function() {
      window.voiceflow.chat.load({
        verify: { projectID: '66ca7eda545e1eff4670f16a' },
        url: 'https://general-runtime.voiceflow.com',
        versionID: 'production'
      });
    }
    v.src = "https://cdn.voiceflow.com/widget/bundle.mjs"; v.type = "text/javascript"; s.parentNode.insertBefore(v, s);
})(document, 'script');