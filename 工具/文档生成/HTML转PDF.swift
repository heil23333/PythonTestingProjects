import AppKit
import Foundation
import WebKit

final class PDFRenderer: NSObject, WKNavigationDelegate {
    private let inputURL: URL
    private let outputURL: URL
    private let webView: WKWebView

    init(inputURL: URL, outputURL: URL) {
        self.inputURL = inputURL
        self.outputURL = outputURL
        let configuration = WKWebViewConfiguration()
        configuration.websiteDataStore = .nonPersistent()
        self.webView = WKWebView(frame: NSRect(x: 0, y: 0, width: 794, height: 1123), configuration: configuration)
        super.init()
        self.webView.navigationDelegate = self
    }

    func start() {
        let directory = inputURL.deletingLastPathComponent()
        let html = (try? String(contentsOf: inputURL, encoding: .utf8)) ?? ""
        webView.loadHTMLString(html, baseURL: directory)
    }

    func webView(_ webView: WKWebView, didFinish navigation: WKNavigation!) {
        DispatchQueue.main.asyncAfter(deadline: .now() + 0.6) {
            webView.evaluateJavaScript("Math.max(document.body.scrollHeight, document.documentElement.scrollHeight)") { result, error in
                if let error {
                    fputs("Failed to measure page: \(error)\n", stderr)
                    exit(1)
                }

                let pageHeight = (result as? NSNumber)?.doubleValue ?? 1123
                let configuration = WKPDFConfiguration()
                configuration.rect = CGRect(x: 0, y: 0, width: webView.bounds.width, height: pageHeight)

                webView.createPDF(configuration: configuration) { result in
                    switch result {
                    case .success(let data):
                        do {
                            try data.write(to: self.outputURL)
                            CFRunLoopStop(CFRunLoopGetMain())
                        } catch {
                            fputs("Failed to write PDF: \(error)\n", stderr)
                            exit(1)
                        }
                    case .failure(let error):
                        fputs("Failed to create PDF: \(error)\n", stderr)
                        exit(1)
                    }
                }
            }
        }
    }
}

if CommandLine.arguments.count != 3 {
    fputs("Usage: html_to_pdf.swift <input.html> <output.pdf>\n", stderr)
    exit(1)
}

let inputURL = URL(fileURLWithPath: CommandLine.arguments[1])
let outputURL = URL(fileURLWithPath: CommandLine.arguments[2])

let app = NSApplication.shared
app.setActivationPolicy(.prohibited)

let renderer = PDFRenderer(inputURL: inputURL, outputURL: outputURL)
renderer.start()
CFRunLoopRun()
