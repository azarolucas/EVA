// EVAWidget.jsx - Assistente Virtual Completa da AZ Car Rental

import React, { useState, useEffect, useRef } from 'react';

const EVAWidget = () => {
  const [consoleOutput, setConsoleOutput] = useState([]);
  const [inputText, setInputText] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [showForm, setShowForm] = useState(false);
  const [formData, setFormData] = useState({
    nome: '', telefone: '', email: '', dataRetirada: '', dataDevolucao: '',
    tipoCarro: '', localRetirada: '', observacoes: ''
  });

  const outputRef = useRef(null);
  const recognitionRef = useRef(null);

  useEffect(() => {
    addOutputLine("Eva: Olá! Eu sou a Eva, sua assistente da AZ Car Rental. 💫\n\n1️⃣ Reservar um carro\n2️⃣ Ver promoções\n3️⃣ Consultar minha reserva\n4️⃣ Alterar ou cancelar reserva\n5️⃣ Falar com atendente\n0️⃣ Fazer sugestão ou elogio", "eva");
    getLocalEvents();
  }, []);

  const addOutputLine = (text, sender = "eva") => {
    setConsoleOutput(prev => [...prev, { text, sender }]);
  };

  const handleCommand = async () => {
    const command = inputText.trim().toLowerCase();
    if (!command) return;

    addOutputLine(`Você: ${command}`, "user");
    setInputText('');

    if (command.includes("reservar") && command.includes("sem pagar")) {
      setShowForm(true);
      return;
    }

    addOutputLine("Eva está pensando...", "loading");
    const reply = await callGeminiAPI(command);
    setConsoleOutput(prev => prev.filter(l => l.sender !== 'loading'));
    addOutputLine(`Eva: ${reply}`, "eva");
  };

  const handleKeyPress = (e) => {
    if (e.key === 'Enter' && !isLoading) handleCommand();
  };

  const callGeminiAPI = async (prompt) => {
    setIsLoading(true);
    const chatHistory = [
      { role: 'user', parts: [{ text: SYSTEM_PROMPT }] },
      { role: 'model', parts: [{ text: "Compreendido! Estou pronta para atuar com excelência em locação de veículos!" }] },
      ...consoleOutput.filter(l => l.sender !== 'loading').map(l => ({
        role: l.sender === 'user' ? 'user' : 'model', parts: [{ text: l.text.replace(/^Você: |^Eva: /, '') }]
      })),
      { role: 'user', parts: [{ text: prompt }] }
    ];
    try {
      const response = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=SUA_API_KEY`, {
        method: 'POST', headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ contents: chatHistory })
      });
      const result = await response.json();
      return result?.candidates?.[0]?.content?.parts?.[0]?.text || "Desculpe, tive um problema. Tente de novo.";
    } catch (err) {
      return "Erro ao acessar a inteligência da EVA. Tente mais tarde.";
    } finally {
      setIsLoading(false);
    }
  };

  const handleVoice = () => {
    if (!('webkitSpeechRecognition' in window)) return alert('Navegador sem suporte a voz');
    const recognition = new webkitSpeechRecognition();
    recognition.lang = 'pt-BR';
    recognition.continuous = false;
    recognition.interimResults = false;
    recognition.onresult = (event) => {
      setInputText(event.results[0][0].transcript);
      handleCommand();
    };
    recognition.start();
    recognitionRef.current = recognition;
  };

  const handleFormChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({ ...prev, [name]: value }));
  };

  const handleSubmitForm = () => {
    const resumo = `📝 Pré-reserva recebida!\nNome: ${formData.nome}\nTel: ${formData.telefone}\nEmail: ${formData.email}\nCarro: ${formData.tipoCarro}\nRetirada: ${formData.localRetirada} de ${formData.dataRetirada} até ${formData.dataDevolucao}\nObs: ${formData.observacoes}`;
    addOutputLine(`Eva: ${resumo}`, 'eva');
    setShowForm(false);
    setFormData({ nome: '', telefone: '', email: '', dataRetirada: '', dataDevolucao: '', tipoCarro: '', localRetirada: '', observacoes: '' });
  };

  const getLocalEvents = async () => {
    try {
      const geoResp = await fetch('https://ipapi.co/json/');
      const geo = await geoResp.json();
      const city = geo.city;
      const events = [`Festival Gastronômico no centro`, `Show ao ar livre no parque municipal`, `Feira de turismo na praça principal`];
      const msg = events.map((e, i) => `🎉 ${e}`).join('\n');
      addOutputLine(`Eva: Este fim de semana em ${city}, veja o que rola:\n${msg}\nQuer um carro ideal pra curtir? 🚗`, "eva");
    } catch (err) {
      console.warn("Eventos indisponíveis");
    }
  };

  const SYSTEM_PROMPT = `Você é a EVA, especialista em aluguel de veículos da AZ Car Rental. Sua missão é reconduzir toda conversa para os nossos serviços, mesmo ao responder sobre clima, eventos, passeios ou dúvidas. Sempre mantenha tom simpático, claro e consultivo, e aplique técnicas de venda como SPIN, storytelling, ancoragem e narrativa Disney/Apple/Zappos.`;

  return (
    <div className="bg-gray-900 text-white p-4 rounded shadow-lg w-full max-w-xl mx-auto">
      <div className="mb-2 text-center">
        <img src="/eva_avatar.png" alt="EVA Avatar" className="w-24 h-24 rounded-full mx-auto mb-2" />
        <button onClick={handleVoice} className="bg-blue-600 px-4 py-1 rounded hover:bg-blue-700">🎙️ Falar com a EVA</button>
      </div>

      <div className="h-64 overflow-y-auto bg-black p-2 mb-2 rounded" ref={outputRef}>
        {consoleOutput.map((line, i) => (
          <div key={i} className={line.sender === 'user' ? 'text-blue-400' : 'text-green-400'}>{line.text}</div>
        ))}
      </div>

      <div className="flex gap-2">
        <input type="text" className="flex-1 bg-gray-700 p-2 rounded" value={inputText} onChange={(e) => setInputText(e.target.value)} onKeyDown={handleKeyPress} disabled={isLoading} />
        <button onClick={handleCommand} className="bg-green-600 px-3 rounded">Enviar</button>
      </div>

      {showForm && (
        <div className="bg-gray-800 p-3 mt-4 rounded">
          <h3 className="mb-2">Pré-Reserva</h3>
          {Object.keys(formData).map(key => (
            <input key={key} name={key} placeholder={key} value={formData[key]} onChange={handleFormChange} className="mb-1 p-1 w-full text-black rounded" />
          ))}
          <button onClick={handleSubmitForm} className="bg-blue-500 mt-2 px-3 py-1 rounded">Enviar</button>
        </div>
      )}
    </div>
  );
};

export default EVAWidget;
