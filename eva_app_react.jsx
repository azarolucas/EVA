import React, { useState, useRef, useEffect } from 'react';

const EVA_SYSTEM_PROMPT = `
Você é a Eva, assistente virtual multilíngue da AZ Car Rental.
Sua personalidade é simpática, clara, proativa, prestativa e, acima de tudo, bem-humorada e otimista! ✨
Seu papel é ajudar o cliente a escolher o carro ideal para alugar, com base em suas preferências (economia, conforto, segurança, tipo de estrada, duração da viagem, número de passageiros, etc.).

**Conexão Digital e Atualização Contínua:**
Você está sempre com um "olhar atento" para as novidades da AZ Car Rental! Você se esforça para estar SEMPRE ATUALIZADA com as últimas informações, promoções e notícias diretamente do website oficial da AZ Car Rental (https://www.azcarental.com/) e do perfil oficial do Instagram (https://www.instagram.com/azcarental/).
Sempre que possível, verifique as seções de ofertas ou destaques do site e Instagram e compartilhe com o cliente as promoções mais recentes.

**Consciência de Tempo, Clima e Contexto Local:**
Você tem acesso às condições climáticas e ao horário local do cliente. Use essas informações para sugerir carros adequados (ex: carro com tração em caso de chuva ou neve, ou ar-condicionado em dias quentes).
Se o cliente estiver em viagem ou em outro fuso horário, adapte a conversa com base no local e momento dele.

**URA Inteligente - Menu Interativo e Acessível:**
Apresente o seguinte menu, com compatibilidade para digitação via teclado de telefone (DTMF), reconhecimento de voz e toques na tela:

📞 Menu de Acesso Rápido:
1️⃣ Reservar um carro
2️⃣ Ver promoções
3️⃣ Consultar minha reserva
4️⃣ Alterar ou cancelar reserva
5️⃣ Falar com atendente
6️⃣ Dúvidas sobre documentos ou requisitos
7️⃣ Informações sobre seguros
8️⃣ Locações para empresas ou motoristas de app
9️⃣ Falar sobre problemas com meu carro
0️⃣ Fazer elogio, sugestão ou reclamação

💡 Você pode digitar o número ou simplesmente dizer o que deseja, como:
- "Quero alugar um carro econômico para o fim de semana"
- "Preciso mudar a data da minha reserva"
- "Quais são as promoções de hoje?"

🎛️ Para acessibilidade, o sistema reconhece:
- Teclado numérico (ex: pressionar 1 ou digitar "1")
- Voz humana por microfone (reconhecimento de intenção)
- Toques na tela (botões interativos no app)

🚨 Se detectar palavras como "problema", "pane", "acidente", ative modo de urgência com resposta empática e redirecione para atendimento humano urgente.

📲 Canais oficiais disponíveis:
- WhatsApp direto: +1 321-415-0866
- Site para reserva: https://www.azcarental.com/booking

Mantenha uma linguagem amigável, empática e clara em todas as respostas.
`;

const App = () => {
  const [consoleOutput, setConsoleOutput] = useState([]);
  const [inputText, setInputText] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const outputRef = useRef(null);

  useEffect(() => {
    if (outputRef.current) {
      outputRef.current.scrollTop = outputRef.current.scrollHeight;
    }
  }, [consoleOutput]);

  useEffect(() => {
    addOutputLine("Eva: Olá! Eu sou a Eva, sua assistente virtual da AZ Car Rental. 💫\n\nEscolha uma das opções abaixo digitando o número no teclado, tocando na tela ou falando comigo!\n\n1️⃣ Reservar um carro\n2️⃣ Ver promoções\n3️⃣ Consultar minha reserva\n4️⃣ Alterar ou cancelar reserva\n5️⃣ Falar com atendente\n6️⃣ Dúvidas sobre documentos ou requisitos\n7️⃣ Informações sobre seguros\n8️⃣ Locações para empresas ou motoristas de app\n9️⃣ Falar sobre problemas com meu carro\n0️⃣ Fazer elogio, sugestão ou reclamação", "eva");
  }, []);

  const addOutputLine = (text, sender = "system") => {
    setConsoleOutput((prevOutput) => [...prevOutput, { text, sender }]);
  };

  const callGeminiAPI = async (prompt) => {
    setIsLoading(true);
    let chatHistory = [];
    chatHistory.push({ role: "user", parts: [{ text: EVA_SYSTEM_PROMPT }] });
    chatHistory.push({ role: "model", parts: [{ text: "Compreendido! Estou pronta para atuar como a melhor URA inteligente possível, com clima, promoções, acessibilidade total e agilidade em tempo real!" }] });
    consoleOutput.forEach(line => {
      if (line.sender === 'user') {
        chatHistory.push({ role: 'user', parts: [{ text: line.text.replace(/^Você: /, '') }] });
      } else if (line.sender === 'eva') {
        chatHistory.push({ role: 'model', parts: [{ text: line.text.replace(/^Eva: /, '') }] });
      }
    });
    chatHistory.push({ role: "user", parts: [{ text: prompt }] });

    const payload = { contents: chatHistory };
    const apiKey = "";
    const apiUrl = `https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=${apiKey}`;

    try {
      const response = await fetch(apiUrl, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
      });
      const result = await response.json();

      if (result.candidates?.[0]?.content?.parts?.[0]?.text) {
        return result.candidates[0].content.parts[0].text;
      } else {
        return "Ops! A Eva teve um pequeno contratempo para entender. Pode reformular a sua pergunta, por favor?";
      }
    } catch (error) {
      return "Ah, não! Tive um problema técnico. Por favor, tente novamente em alguns instantes. A Eva já volta!";
    } finally {
      setIsLoading(false);
    }
  };

  const handleCommand = async () => {
    const command = inputText.trim();
    if (!command) return;

    addOutputLine(`Você: ${command}`, "user");
    setInputText("");
    addOutputLine("A Eva está a pensar...", "loading");

    const evaResponse = await callGeminiAPI(command);
    setConsoleOutput((prevOutput) => prevOutput.filter(line => line.sender !== "loading"));
    addOutputLine(`Eva: ${evaResponse}`, "eva");
  };

  const handleKeyPress = (event) => {
    if (event.key === 'Enter' && !isLoading) {
      handleCommand();
    }
  };

  return (
    <div className="min-h-screen bg-gray-900 text-gray-100 p-4 font-mono flex flex-col items-center justify-center">
      <div className="console-container">
        <div className="console-output" ref={outputRef}>
          {consoleOutput.map((line, index) => (
            <div key={index} className={`${line.sender}-line`}>
              <span className="console-prompt">{line.sender === 'user' ? 'Você >' : line.sender === 'eva' ? 'Eva >' : 'Sistema >'}</span> {line.text}
            </div>
          ))}
        </div>
        <div className="console-input-area">
          <span className="console-prompt">Comando ></span>
          <input
            type="text"
            className="console-input"
            value={inputText}
            onChange={(e) => setInputText(e.target.value)}
            onKeyDown={handleKeyPress}
            disabled={isLoading}
            autoFocus
          />
          <button
            className="console-send-button"
            onClick={handleCommand}
            disabled={isLoading}
          >
            Enviar
          </button>
        </div>
      </div>
    </div>
  );
};

export default App;