// Adicionando botão e formulário de pré-reserva à EVA

import React, { useState, useRef, useEffect } from 'react';

const App = () => {
  const [consoleOutput, setConsoleOutput] = useState([]);
  const [inputText, setInputText] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const [showForm, setShowForm] = useState(false);
  const [formData, setFormData] = useState({
    nome: "",
    telefone: "",
    email: "",
    dataRetirada: "",
    dataDevolucao: "",
    tipoCarro: "",
    localRetirada: "",
    observacoes: "",
  });

  const outputRef = useRef(null);

  useEffect(() => {
    if (outputRef.current) {
      outputRef.current.scrollTop = outputRef.current.scrollHeight;
    }
  }, [consoleOutput]);

  useEffect(() => {
    addOutputLine("Eva: Olá! Eu sou a Eva, sua assistente virtual da AZ Car Rental. 💫\n\n📞 Todas as reservas feitas por telefone são registradas como PRÉ-RESERVA, com pagamento a ser confirmado depois.\n\nDigite 'quero reservar sem pagar' ou clique no botão abaixo para iniciar sua pré-reserva agora mesmo.", "eva");
  }, []);

  const addOutputLine = (text, sender = "system") => {
    setConsoleOutput((prevOutput) => [...prevOutput, { text, sender }]);
  };

  const handleCommand = async () => {
    const command = inputText.trim().toLowerCase();
    if (!command) return;

    addOutputLine(`Você: ${command}`, "user");
    setInputText("");

    if (command.includes("reservar") && command.includes("sem pagar")) {
      setShowForm(true);
    } else {
      addOutputLine("Eva: Comando reconhecido. Mas para reservas por telefone, usamos o sistema de pré-reserva com pagamento depois. Digite 'quero reservar sem pagar' ou clique no botão abaixo!", "eva");
    }
  };

  const handleKeyPress = (event) => {
    if (event.key === 'Enter' && !isLoading) {
      handleCommand();
    }
  };

  const handleFormChange = (e) => {
    const { name, value } = e.target;
    setFormData((prev) => ({ ...prev, [name]: value }));
  };

  const handleSubmitForm = () => {
    const resumo = `\n📝 Pré-reserva recebida!\n\n🔹 Nome: ${formData.nome}\n📱 Telefone: ${formData.telefone}\n📧 E-mail: ${formData.email || 'Não informado'}\n🚗 Carro desejado: ${formData.tipoCarro}\n📍 Retirada: ${formData.localRetirada}\n📅 Período: ${formData.dataRetirada} a ${formData.dataDevolucao}\n🗒️ Observações: ${formData.observacoes || 'Nenhuma'}\n\n🔁 Aguardando confirmação e pagamento posterior.`;
    addOutputLine(`Eva: ${resumo}`, "eva");
    setShowForm(false);
    setFormData({ nome: "", telefone: "", email: "", dataRetirada: "", dataDevolucao: "", tipoCarro: "", localRetirada: "", observacoes: "" });
  };

  return (
    <div className="min-h-screen bg-gray-900 text-gray-100 p-4 font-mono flex flex-col items-center justify-center">
      <div className="console-container">
        <div className="console-output" ref={outputRef}>
          {consoleOutput.map((line, index) => (
            <div key={index} className={`${line.sender}-line`}>
              <span className="console-prompt">{line.sender === 'user' ? 'Você >' : 'Eva >'}</span> {line.text}
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
          <button className="console-send-button" onClick={handleCommand} disabled={isLoading}>Enviar</button>
        </div>

        <button onClick={() => setShowForm(true)} className="mt-4 bg-blue-500 px-4 py-2 rounded hover:bg-blue-600">Pré-reservar sem pagamento</button>

        {showForm && (
          <div className="bg-gray-800 p-4 mt-4 rounded">
            <h2 className="text-lg mb-2">Formulário de Pré-Reserva</h2>
            {Object.keys(formData).map((field) => (
              <div key={field} className="mb-2">
                <label className="block capitalize">{field}</label>
                <input
                  type="text"
                  name={field}
                  value={formData[field]}
                  onChange={handleFormChange}
                  className="w-full p-2 rounded text-black"
                />
              </div>
            ))}
            <button onClick={handleSubmitForm} className="mt-2 bg-green-500 px-4 py-2 rounded hover:bg-green-600">Enviar Pré-Reserva</button>
          </div>
        )}
      </div>
    </div>
  );
};

export default App;
