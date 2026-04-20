<!DOCTYPE html>
<html>
<head>
    <title>Loan Prediction System</title>

    <style>
        body {
            font-family: 'Segoe UI', sans-serif;
            background: linear-gradient(135deg, #667eea, #764ba2);
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        .container {
            background: rgba(255, 255, 255, 0.15);
            backdrop-filter: blur(12px);
            padding: 40px;
            border-radius: 20px;
            width: 380px;
            box-shadow: 0 8px 32px rgba(0,0,0,0.3);
            text-align: center;
            color: white;
            animation: fadeIn 1s ease-in-out;
        }

        h2 {
            font-size: 28px;
            margin-bottom: 20px;
            letter-spacing: 1px;
        }

        input, select {
            width: 100%;
            padding: 14px;
            margin: 10px 0;
            border: none;
            border-radius: 10px;
            font-size: 16px;
            outline: none;
        }

        input:focus, select:focus {
            transform: scale(1.03);
            transition: 0.2s;
        }

        button {
            width: 100%;
            padding: 14px;
            background: #00c9ff;
            background: linear-gradient(to right, #00c9ff, #92fe9d);
            border: none;
            border-radius: 10px;
            font-size: 18px;
            font-weight: bold;
            color: black;
            cursor: pointer;
            margin-top: 10px;
            transition: 0.3s;
        }

        button:hover {
            transform: scale(1.05);
            box-shadow: 0 0 15px rgba(255,255,255,0.4);
        }

        h3 {
            margin-top: 20px;
            font-size: 22px;
            animation: fadeIn 0.5s ease-in;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(-10px); }
            to { opacity: 1; transform: translateY(0); }
        }
    </style>
</head>

<body>

<div class="container">
    <h2>💰 Loan Prediction</h2>

    <form action="/predict" method="post">

        <input type="number" name="income" placeholder="Enter Income" required>

        <input type="number" name="credit" placeholder="Credit Score" required>

        <select name="employment" required>
            <option>Employed</option>
            <option>Self-Employed</option>
            <option>Unemployed</option>
        </select>

        <input type="number" name="loan" placeholder="Loan Amount" required>

        <button type="submit">Predict Loan</button>

    </form>

    <h3>{{ prediction }}</h3>
</div>

</body>
</html>