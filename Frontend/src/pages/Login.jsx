import { useState, useContext } from "react";
//importing custom css
import "../App.css";
import "bootstrap/dist/css/bootstrap.min.css";

import { Link } from "react-router-dom";
import { AuthContext } from "../contexts/AuthContext";
import { useNavigate } from "react-router-dom";
import { FaEye, FaEyeSlash } from "react-icons/fa";

function Login() {
  const { login } = useContext(AuthContext);
  const [emailOrPhone, setEmailOrPhone] = useState("");
  const [password, setPassword] = useState("");
  const [loading, setLoading] = useState(false);
  const [validated, setValidated] = useState(false);
  const [showPassword, setShowPassword] = useState(false);
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    const form = e.currentTarget;

    if (!form.checkValidity()) {
      setValidated(true);
      return;
    }
    setLoading(true);

    const result = await login(emailOrPhone, password);
    if (!result.success) {
      navigate("/", {
        state: { toast: { type: "error", message: result.message } },
      });
      setLoading(false);
    } else {
      navigate("/dashboard", {
        state: { toast: { type: "success", message: result.message } },
      });
    }
  };

  return (
    <>
      <div
        className="container d-flex flex-column justify-content-center align-items-center vh-100"
        style={{ marginTop: "-2rem" }} // Move the entire container up
      >
        <img
          src="/kmc_logo.png" // Replace with the actual path to your PNG
          alt="KMC Logo"
          style={{ maxWidth: "200px", marginBottom: "0.5rem" }} // Adjust spacing above and below the logo
        />
        <h1
          className="text-center"
          style={{ color: "var(--heading-color)", marginBottom: "0.5rem" }} // Adjust spacing below the h1
        >
          Kathmandu Metropolitian City
        </h1>
        <div
          className="card p-4 shadow"
          style={{
            maxWidth: "400px",
            width: "100%",
            height: "auto", // Allow the container to grow vertically
            backgroundColor: "var(--card-bg)",
            borderColor: "var(--card-border)",
            boxShadow: `0 4px 6px var(--card-shadow)`,
          }}
        >
          <h4
            className="text-center text-muted"
            style={{ color: "var(--text-light)" }}
          >
            Sign in to your account
          </h4>
          <form
            noValidate
            className={validated ? "was-validated" : ""}
            onSubmit={handleSubmit}
          >
            <div className="mb-3">
              <label
                htmlFor="email"
                className="form-label"
                style={{ color: "var(--text-color)" }}
              >
                Email/Username/Ph no.
              </label>
              <input
                type="text"
                id="email"
                className="form-control"
                placeholder="Enter your ID"
                style={{
                  border: "2px solid",
                  borderColor: "var(--input-border)",
                }}
                onMouseEnter={(e) =>
                  (e.target.style.borderColor = "var(--primary-color)")
                }
                onMouseLeave={(e) =>
                  (e.target.style.borderColor = "var(--input-border)")
                }
                value={emailOrPhone}
                onChange={(e) => setEmailOrPhone(e.target.value)}
                required
              />
              <div className="invalid-feedback">
                Email or phone is required.
              </div>
            </div>

            <div className="mb-3">
              <label
                htmlFor="password"
                className="form-label"
                style={{ color: "var(--text-color)" }}
              >
                Password
              </label>
              <div className="input-group">
                <input
                  type={showPassword ? "text" : "password"}
                  id="password"
                  className="form-control"
                  placeholder="Enter your password"
                  style={{
                    border: "2px solid",
                    borderColor: "var(--input-border)",
                  }}
                  onMouseEnter={(e) =>
                    (e.target.style.borderColor = "var(--primary-color)")
                  }
                  onMouseLeave={(e) =>
                    (e.target.style.borderColor = "var(--input-border)")
                  }
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  required
                />
                <span
                  onClick={() => setShowPassword(!showPassword)}
                  className="input-group-text"
                  style={{
                    cursor: "pointer",
                    backgroundColor: "#fff",
                    borderLeft: "0",
                    borderRadius: "0px 5px 5px 0px",
                    border: ".1rem solid var(--input-border)",
                    color: "var(--text-light)",
                  }}
                >
                  {showPassword ? <FaEyeSlash /> : <FaEye />}
                </span>
                <div className="invalid-feedback">Password is required.</div>
              </div>
            </div>

            <div className="d-flex justify-content-between align-items-center mb-3">
              <div className="form-check">
                <input
                  type="checkbox"
                  className="form-check-input"
                  id="remember"
                />
                <label
                  className="form-check-label"
                  htmlFor="remember"
                  style={{ color: "var(--text-color)" }}
                >
                  Remember me
                </label>
              </div>
              <a
                href="#"
                className="text-decoration-underline"
                style={{ color: "var(--primary-color)" }}
              >
                Forgot password?
              </a>
            </div>

            <button
              type="submit"
              className="btn w-100 mb-2"
              style={{
                backgroundColor: "var(--btn-primary-bg)",
                color: "var(--btn-text)",
              }}
              onMouseEnter={(e) =>
                (e.target.style.backgroundColor = "var(--btn-primary-hover)")
              }
              onMouseLeave={(e) =>
                (e.target.style.backgroundColor = "var(--btn-primary-bg)")
              }
              disabled={loading}
            >
              {loading ? "Logging in..." : "Login"}
            </button>
            <button
              type="button"
              className="btn w-100"
              style={{
                backgroundColor: "var(--btn-primary-bg)",
                color: "var(--btn-text)",
                marginTop: "1.3rem",
              }}
              onMouseEnter={(e) =>
                (e.target.style.backgroundColor = "var(--btn-primary-hover)")
              }
              onMouseLeave={(e) =>
                (e.target.style.backgroundColor = "var(--btn-primary-bg)")
              }
            >
              Digital Signature Login
            </button>
          </form>
        </div>
      </div>
    </>
  );
}

export default Login;
