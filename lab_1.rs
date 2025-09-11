use std::env;
use std::io;
use std::io::Write;
use std::process;

struct Coefficients {
    a: f64,
    b: f64,
    c: f64,
}

impl Coefficients {
    fn get() -> Result<Coefficients, String> {
        let args: Vec<String> = env::args().collect();
        
        if args.len() > 4 {
            return Err("Слишком много коэффициентов. Пожалуйста, перезапустите программу.".to_string());
        }
        
        let mut coefficients = Coefficients { a: 0.0, b: 0.0, c: 0.0 };
        let coefficient_names = ["a", "b", "c"];
        
        for i in 0..3 {
            let value = if i + 1 < args.len() {
                match args[i + 1].parse::<f64>() {
                    Ok(val) => val,
                    Err(_) => {
                        return Err("Коэффициенты должны быть числами.".to_string());
                    }
                }
            } else {
                print!("Введите коэффициент {}: ", coefficient_names[i]);
                io::stdout().flush().unwrap();
                
                let mut input = String::new();
                io::stdin().read_line(&mut input).unwrap();
                
                match input.trim().parse::<f64>() {
                    Ok(val) => val,
                    Err(_) => {
                        return Err("Коэффициенты должны быть числами.".to_string());
                    }
                }
            };
            
            match i {
                0 => coefficients.a = value,
                1 => coefficients.b = value,
                2 => coefficients.c = value,
                _ => (),
            }
        }
        
        Ok(coefficients)
    }
}

fn solve_biquadratic(a: f64, b: f64, c: f64) -> (String, Vec<f64>) {
    if a == 0.0 {
        if b == 0.0 {
            if c == 0.0 {
                return ("Уравнение имеет бесконечно много решений.".to_string(), Vec::new());
            } else {
                return ("Уравнение не имеет решений.".to_string(), Vec::new());
            }
        } else {
            let t = -c / b;
            if t < 0.0 {
                return ("Действительных решений нет.".to_string(), Vec::new());
            } else if t == 0.0 {
                return ("Одно решение: x = 0".to_string(), vec![0.0]);
            } else {
                let root1 = -t.sqrt();
                let root2 = t.sqrt();
                return (format!("Два решения: x = {}, x = {}", root1, root2), vec![root1, root2]);
            }
        }
    }
    let discriminant = b * b - 4.0 * a * c;
    
    if discriminant < 0.0 {
        return ("Действительных решений нет.".to_string(), Vec::new());
    } else if discriminant == 0.0 {
        let t = -b / (2.0 * a);
        if t < 0.0 {
            return ("Действительных решений нет.".to_string(), Vec::new());
        } else if t == 0.0 {
            return ("Одно решение: x = 0".to_string(), vec![0.0]);
        } else {
            let root1 = -t.sqrt();
            let root2 = t.sqrt();
            return (format!("Два решения: x = {}, x = {}", root1, root2), vec![root1, root2]);
        }
    } else {
        let t1 = (-b - discriminant.sqrt()) / (2.0 * a);
        let t2 = (-b + discriminant.sqrt()) / (2.0 * a);
        
        let mut roots = Vec::new();
        if t1 >= 0.0 {
            if t1 == 0.0 {
                roots.push(0.0);
            } else {
                roots.push(-t1.sqrt());
                roots.push(t1.sqrt());
            }
        }
        if t2 >= 0.0 {
            if t2 == 0.0 {
                if !roots.contains(&0.0) {
                    roots.push(0.0);
                }
            } else {
                roots.push(-t2.sqrt());
                roots.push(t2.sqrt());
            }
        }
        roots.sort_by(|a, b| a.partial_cmp(b).unwrap());
        roots.dedup_by(|a, b| a == b);
        
        if roots.is_empty() {
            return ("Действительных решений нет.".to_string(), Vec::new());
        } else if roots.len() == 1 {
            return (format!("Одно решение: x = {}", roots[0]), roots);
        } else {
            let roots_str = roots.iter()
                .map(|r| format!("x = {}", r))
                .collect::<Vec<String>>()
                .join(", ");
            return (format!("Решения: {}", roots_str), roots);
        }
    }
}

fn main() {
    println!("Решение биквадратного уравнения a*x^4 + b*x^2 + c = 0");
    let coefficients = match Coefficients::get() {
        Ok(coeffs) => coeffs,
        Err(err) => {
            eprintln!("Ошибка: {}", err);
            process::exit(1);
        }
    };
    let (message, roots) = solve_biquadratic(coefficients.a, coefficients.b, coefficients.c);
    println!("{}", message);
}