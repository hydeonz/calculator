#!/bin/bash

Menu() {
    echo "Choose action:"
    echo "1. Download actual dev-version of app"
    echo "2. Run app"
    echo "3. Run Unit-Tests"
    echo "4. Build installer"
    echo "5. Upload artifact"

    read -p "Enter your choice: " choice

    case $choice in
        1)
            LoadDevVersion
            ;;
        2)
            RunApplication
            ;;
        3)
            RunUnitTests
            ;;
        4)
            BuildApplication
            ;;
        5)
            UploadArtifact
            ;;
        *)
            echo "Enter a valid answer"
            ;;
    esac

    read -p "Would you like to continue? (Y/N): " continue
    if [[ "$continue" =~ ^[Yy]$ ]]; then
        Menu
    else
        exit 0
    fi
}

LoadDevVersion() {
    rm -rf calculator
    echo "Cloning repository..."
    git clone https://github.com/hydeonz/calculator
    echo "Downloading dependencies..."
    pip install -r calculator/reqs.txt
    Menu
}

RunApplication() {
    echo "Launching app..."
    python3 calculator/calc.py
    Menu
}

RunUnitTests() {
    echo "Launching unit tests..."
    python3 calculator/unit_test_v2.py
    Menu
}

BuildApplication() {
    echo "Building..."
    cd calculator || exit
    python3 setup.py sdist
    cd ..
    Menu
}

UploadArtifact() {
    echo "Uploading..."
    cd calculator/dist || exit
    pip install calculator-1.0.tar.gz
    cd ../..
    Menu
}

Menu
