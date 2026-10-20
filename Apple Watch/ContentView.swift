import SwiftUI

struct ContentView: View {
    var body: some View {
        VStack(spacing: 8) {
            Image(systemName: "heart.fill")
                .font(.largeTitle)
                .foregroundStyle(.pink)

            Text("Hello, world!")
                .font(.headline)
                .multilineTextAlignment(.center)

            Text("PartnerPush")
                .font(.caption2)
                .foregroundStyle(.secondary)
        }
        .padding()
    }
}

#Preview {
    ContentView()
}