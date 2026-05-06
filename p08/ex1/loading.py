import importlib.util
import importlib.metadata


def check_dependencies() -> bool:
    print("Checking dependencies:")

    packages = {"pandas": "Data manipulation ready",
                "numpy": "Numerical computation ready",
                "requests": "Network access ready",
                "matplotlib": "Visualization ready"
                }
    all_ok = True

    def module_check(module: str) -> bool:
        try:
            importlib.import_module(module)
            return True
        except Exception:
            return False

    def version_check(vers: str) -> str:
        version: str = str(importlib.import_module(vers).__version__)
        return version

    for package, msg in packages.items():
        spec = module_check(package)
        if spec is False:
            print(f"[MISSING] {package}")
            print(f"  pip:  pip install {package}")
            print(f"  Poetry:  poetry add {package}")
            all_ok = False
        else:
            print(f'[OK] {package} {version_check(package)} - {msg}')
    return all_ok


def analyse() -> None:
    import numpy as np
    import matplotlib.pyplot as plt

    print("Analyzing Matrix data...")

    data = np.random.randn(1000)
    print("Processing 1000 data points...")

    print("Generating visualization...\n")
    plt.figure(figsize=(10, 6))
    plt.hist(data, bins=30, color='green', edgecolor='black')
    plt.title('Matrix Data Distribution')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.savefig('matrix_analysis.png')
    plt.close()

    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


def main() -> None:
    print("LOADING STATUS: Loading programs...\n")

    if not check_dependencies():
        return
    else:
        analyse()


if __name__ == "__main__":
    main()
