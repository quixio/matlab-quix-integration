# MATLAB Quix Integration

Quix enables developers to run MATLAB code in real-time streaming pipelines.  
This repository brings together different integration options, depending on your needs and MATLAB version.

## Why This Project?

MATLAB is a powerful environment for numerical computing, but deploying MATLAB functions into streaming pipelines is not always straightforward. With Quix, you can:

- Stream input data from Kafka topics
- Run MATLAB code in real time
- Publish transformed results back to Kafka

## Available Integration Options

We provide three templates, showcasing two different integration strategies:

1. **MATLAB Wheel [Template](https://github.com/quixio/matlab-quix-integration/tree/main/matlab-wheel)**  
   Recommended. Compile MATLAB functions into Python-compatible `.whl` packages and run them seamlessly inside Quix.

2. **MATLAB Engine [2023b](https://github.com/quixio/matlab-quix-integration/tree/main/matlab-docker-2023b) | [2025a](https://github.com/quixio/matlab-quix-integration/tree/main/matlab-docker-2025a)**  
   Run MATLAB functions directly in Quix using a MATLAB Engine instance. Examples provided both for 2023b and 2025a versions.


#### MATLAB Engine VS MATLAB Wheel

| Method          | Advantages | Disadvantages                                                                                                                          |
|-----------------|------------|----------------------------------------------------------------------------------------------------------------------------------------|
| **MATLAB Wheel** | - Compiles MATLAB code into Python (`.whl`) → portable<br>- No MATLAB license needed at runtime (only at build)<br>- Lightweight deployment in Quix | - Extra build step needed <br> (altough made easy with `quix_compiler.m`)                                                              |
| **MATLAB Engine** | - Directly runs `.m` files without extra build step<br>- Closer to MATLAB environment (no translation)<br>- Easier when iterating and testing | - Requires MATLAB license server in runtime<br>- Heavier runtime footprint<br>- Harder to deploy in lightweight/cloud-native scenarios |

---

## Contribution

We welcome contributions!  
- Submit forked projects to the [Quix GitHub repo](https://github.com/quixio).  
- Accepted projects will be attributed to you and you’ll receive **$200 in Quix credit**. 🎉

## License

This project is open source under the **Apache 2.0 license**.  
⭐ Please star us and mention us on social to show your appreciation.